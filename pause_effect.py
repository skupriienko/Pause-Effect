# -*- coding: utf-8 -*-
"""pause_effect.py
"""

# pip install nltk

import re
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
stopwords = stopwords.words('english')
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# %matplotlib inline
import seaborn as sns


python = """
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
 
The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
 
The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.
 
This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.
 
For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.
 
This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.
 
"""

def clean_with_regex(text):
    clean_endlines = re.sub("\.\n", '.+++', text)
    clean_endlines = re.sub("!\n", '!+++', clean_endlines)
    clean_endlines = re.sub(":\n", '+++', clean_endlines)
    clean_endlines = re.sub("\n", ' ', clean_endlines)
    enter_endlines = re.sub("\+{3}", "\n", clean_endlines)
    return enter_endlines


cleaned_text_list = []
corpora_cleaned = clean_with_regex(python)
corpora_lower = corpora_cleaned.lower()
match_words = re.findall(r"\b[A-Za-z']+\b(?=[,\.!\?:;\"—]+)", corpora_lower, re.I)
text = [word for word in match_words if word not in stopwords]

most_common_words = []
fdist = FreqDist(text)
most_common = fdist.most_common(20)
most_common_words.append(most_common)
x = [word[0] for word in most_common]
y = [word[1] for word in most_common]

sns.set(font='DejaVu Sans',
        rc={
 'axes.axisbelow': False,
 'axes.edgecolor': 'lightgrey',
 'axes.facecolor': '#d6e3f8',
 'axes.grid': False,
 'axes.labelcolor': '#002855',
 'axes.spines.right': False,
 'axes.spines.top': False,
 'figure.facecolor': 'white',
 'lines.solid_capstyle': 'round',
 'patch.edgecolor': 'w',
 'patch.force_edgecolor': True,
 'text.color': '#001845',
 'xtick.bottom': False,
 'xtick.color': '#33415c',
 'xtick.direction': 'out',
 'xtick.top': False,
 'ytick.color': '#001233',
 'ytick.direction': 'out',
 'ytick.left': False,
 'ytick.right': False})
sns.set_context("notebook", rc={"font.size":16,
                                "axes.titlesize":20,
                                "axes.labelsize":18})
plt.legend(frameon=False)
sns.despine(left=True, bottom=True)

fig, ax = plt.subplots(figsize=(20, 5))
# fig.set_facecolor(color_bg)
ax.scatter(x, y, alpha=0.70, marker='v', c=y, cmap=cm.brg)
# fig.text(x=0.8, y=0.95, s='kuprienko.info', horizontalalignment='left', color='#7d8597')
ax.set_title('The Pause Effect + 20 Most common words of "Python Tutorial"')
ax.set_xlabel('Words')
ax.set_ylabel('Frequency')
#removing top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#adds major gridlines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.show()
fig.savefig('python')
