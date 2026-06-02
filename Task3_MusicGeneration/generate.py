import glob
import numpy as np
from music21 import instrument, note, stream, chord, converter
from keras.models import load_model

print("Loading teri AI...")
model = load_model('music_model.h5')

def get_notes():
    notes = []
    for file in glob.glob("midi_songs/*.mid"):
        print(f"Reading {file}")
        try:
            midi = converter.parse(file)
            # Ye line sabse important hai - har note pakdegi
            notes_to_parse = midi.flat.notesAndRests
            
            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
        except Exception as e:
            print(f"Error in {file}: {e}")
            
    return notes

print("Training data se notes nikaal rahi hu...")
notes = get_notes()

print(f"Total notes mile: {len(notes)}")
if len(notes) < 50:
    print("ERROR: MIDI files me notes bahut kam hain!")
    print("Google pe 'Bach Inventions MIDI' download karke midi_songs me daal")
    exit()

pitchnames = sorted(set(item for item in notes))
n_vocab = len(pitchnames)
note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

sequence_length = 50 if len(notes) < 200 else 100

start = np.random.randint(0, len(notes) - sequence_length)
pattern = [note_to_int[notes[i]] for i in range(start, start + sequence_length)]

print("AI music bana rahi hai...")
prediction_output = []

for note_index in range(500):
    prediction_input = np.reshape(pattern, (1, sequence_length, 1))
    prediction_input = prediction_input / float(n_vocab)
    
    prediction = model.predict(prediction_input, verbose=0)
    index = np.argmax(prediction)
    result = int_to_note[index]
    prediction_output.append(result)
    
    pattern.append(index)
    pattern = pattern[1:]

print("MIDI file bana rahi hu...")
offset = 0
output_notes = []

for pattern in prediction_output:
    if ('.' in pattern) or pattern.isdigit():
        notes_in_chord = pattern.split('.')
        notes_list = []
        for current_note in notes_in_chord:
            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            notes_list.append(new_note)
        new_chord = chord.Chord(notes_list)
        new_chord.offset = offset
        output_notes.append(new_chord)
    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)
    
    offset += 0.5

midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='my_ai_music.mid')
print("DONE! my_ai_music.mid file ban gayi ✅")
print("Double click karke sun teri AI ka pehla gaana 🎵")