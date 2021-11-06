import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from matplotlib.colors import LinearSegmentedColormap



if __name__ == "__main__":
    df = pd.read_csv('./content/trump_tweets.csv')
    # print(df.head()) #print the first 4 row
    # print(df.isnull().sum()) #check for null col
    tweets = " ".join(line for line in df['text'])

    mask = np.array(Image.open("./content/mask.png"))
    colors = ["#BF0A30", "#002868"]
    cmap = LinearSegmentedColormap.from_list("mycmap", colors)

    stop_words = set(STOPWORDS)
    stop_words.update(["https","t","s","will","now"])
    # print(stop_words)
    wc = WordCloud(width = 600, height = 400, random_state=1, background_color='white', colormap=cmap , mask=mask, collocations=True, stopwords = stop_words).generate(tweets)

    plt.figure(figsize=[5,5])
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    plt.show()