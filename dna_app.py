import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# 1. App की सेटिंग
st.set_page_config(page_title='DNA Count App', layout='wide')

# 2. फोटो लोड करना (dna_pic.jpg)
try:
    image = Image.open('dna_pic.jpg')
    st.image(image, use_container_width=True)
except FileNotFoundError:
    st.warning("Warning: 'dna_pic.jpg' नहीं मिली। कृपया चेक करें कि फोटो उसी फोल्डर में है या नहीं।")

# 3. टाइटल और डिस्क्रिप्शन
st.write("""
# DNA Nucleotide Count Web App
यह ऐप DNA सीक्वेंस को इनपुट लेता है और Nucleotide (A, T, G, C) की गिनती करता है।
***
""")

# 4. इनपुट बॉक्स
st.header('Enter DNA Sequence')

sequence_input = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCTGATACACAAGTCAGTAGTGGAGTCTCTTGTCCCTCTTGTCTTCGTTTCGATCTCTCCTCTCATTGTCTCTGTCACATCAGCATCTA"

sequence = st.text_area("Sequence Input", sequence_input, height=150)

# 5. डेटा सफाई (Cleaning)
sequence = sequence.splitlines()
sequence = sequence[1:] # पहली लाइन हटाओ
sequence = ''.join(sequence) # बाकी लाइन जोड़ो
sequence = sequence.upper() # बड़े अक्षरों में बदलो

st.write("""
***
""")

# 6. आउटपुट दिखाना
st.header('INPUT (DNA Query)')
st.text(sequence)

st.header('OUTPUT (DNA Nucleotide Count)')

# 7. गिनती का लॉजिक function
def DNA_nucleotide_count(seq):
    d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
            ])
    return d

X = DNA_nucleotide_count(sequence)

# 8. परिणाम 1: Dictionary
st.subheader('1. Dictionary Format')
st.write(X)

# 9. परिणाम 2: Text
st.subheader('2. Text Format')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# 10. परिणाम 3: DataFrame
st.subheader('3. DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# 11. परिणाम 4: Bar Chart
st.subheader('4. Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count',
    color='nucleotide'
).properties(
    width=alt.Step(80)
)
st.write(p)