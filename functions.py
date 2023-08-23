
    #if selected_user =='overall':
        #fetch number of messages
       # num_messages = df.shape[0]
        #number of words
        #words= []
        #for message in df['message']:
         #   words.extend(message.split())

        #num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]
        #return num_messages, len(words),num_media_messages
    #else:
     #   new_df = df[df['user']== selected_user]
      #  num_messages = new_df.shape[0]
       # words= []
        #for message in new_df['message']:
         #   words.extend(message.split())

       # return num_messages, len(words) 
# efficient code for above code
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
import re
from textblob import TextBlob
from collections import Counter


extractor = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    # fetch numbers
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    #fetch number of media messages 
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    #fetch number of links shared
    links = []

    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df= round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns=
                                                                                {'index':'name','user':'percentage'} )
    return x,df


def create_wordcloud(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    
    
    wc = WordCloud(width=500, height=500, min_font_size= 10, background_color ='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):

    f = open('stop_hinglish.txt','r')
    stop_words =f.read()
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    
    return_df = pd.DataFrame(Counter(words).most_common(20))  

    return return_df

def monthly_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    timeline= df.groupby(['year','month_num','month']).count()['message'].reset_index()
    time =[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))
    timeline['time'] = time
    return timeline


def daily_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('Date').count()['message'].reset_index()

    return daily_timeline


def week_activity_map(selected_user, df):

    if selected_user != 'overall':
         df = df[df['user'] == selected_user]

    return_1 = df['day_name'].value_counts()
    return return_1


def month_activity_map(selected_user, df):

    if selected_user != 'overall':
         df = df[df['user'] == selected_user]

    return_2 = df['month'].value_counts()
    return return_2


def activity_heatmap(selected_user, df):
    if selected_user != 'overall':
         df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name',columns='period', values = 'message',aggfunc='count').fillna(0)
    return user_heatmap



def emoji_helper(selected_user,df):
    if selected_user != 'overall':
         df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    emoji_df =  pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df    


def classify_emojis(emojis):
    # Create a dictionary mapping emojis to emotions (customize as needed)
    emoji_emotion_mapping = {
        '😡': 'anger',
        '😐': 'bored',
        '😄': 'happiness',
        '😢': 'sadness',
        '😱': 'fear',
        '😃': 'excited'
    }

    classified_emojis = [emoji_emotion_mapping.get(emoji, 'unknown') for emoji in emojis]
    return classified_emojis

def translate_and_classify_emotion(sentences):
    emotion_scores = []

    for sentence in sentences:
        text_blob = TextBlob(sentence)
        sentiment_score = text_blob.sentiment.polarity

        # Classify emotions based on sentiment scores (customize as needed)
        if sentiment_score < -0.1:
            emotion = 'negative'
        elif sentiment_score > 0.1:
            emotion = 'positive'
        else:
            emotion = 'neutral'

        emotion_scores.append(emotion)

    return emotion_scores

def calculate_final_scores(df):
    # Calculate emoji scores based on their emotions (customize scoring as needed)
    emoji_scores = df['emoji_emotion'].apply(lambda x: 2 if x == 'happiness' else -1)

    # Calculate sentence scores based on emotion (customize scoring as needed)
    sentence_scores = df['sentence_emotion'].apply(lambda x: 1 if x == 'positive' else -1)

    # Calculate total scores
    df['total_score'] = emoji_scores + sentence_scores

    return df



def calculate_emoji_category_scores(df):
    emoji_categories = {
        "angry": ["😡", "🤬", "😤"],
        "bored": ["😑", "😒"],
        "excitement": ["😃", "😄", "😁"],
        "fear": ["😱", "😨", "😰"],
        "happy": ["😊", "😄", "🙂"],
        "sad": ["😞", "😢", "😭"]
    }

     # Create a dictionary to store scores for each category
    emoji_category_scores = {category: 0 for category in emoji_categories}

    for _, row in df.iterrows():
        for category, emojis in emoji_categories.items():
            for emoji_char in emojis:
                if emoji_char in row['message']:
                    emoji_category_scores[category] += 1

    return emoji_category_scores






    


  
  

