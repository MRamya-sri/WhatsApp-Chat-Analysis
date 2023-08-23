import streamlit as st
import preprocessor
import functions
import matplotlib.pyplot as plt
import seaborn as sns
import emoji
from functions import calculate_emoji_category_scores

plt.rcParams['font.family'] = 'DejaVu Sans'

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "overall")

    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words, num_media_messages, links = functions.fetch_stats(selected_user, df)

        col1, col2, col3, col4 = st.columns(4)
        st.title("TOP STATISTICS")

        with col1:
            st.header("Total Messages ")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.title(links)

        # Monthly timeline
        st.title("Monthly Timeline")
        timeline = functions.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Daily timeline
        st.title("Daily Timeline")
        timeline = functions.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['Date'], timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        st.dataframe(timeline)

        # Activity map
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = functions.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = functions.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Activity heatmap
        st.title("Weekly Activity")
        user_heatmap = functions.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        if selected_user == 'overall':
            st.title('Most Busy Users')
            x, new_df = functions.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='blue')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # Emoji analysis
        st.title("Emoji Analysis")
        emoji_df = functions.emoji_helper(selected_user, df)

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
            st.pyplot(fig)

        # Word cloud
        st.title("Word Cloud")
        df_wc = functions.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most common words
        most_common_df = functions.most_common_words(selected_user, df)

        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1], color='magenta')
        plt.xticks(rotation='vertical')
        st.title("Most Common Words and Emojis")
        st.pyplot(fig)
        st.dataframe(most_common_df)

        # Calculate emoji category scores
        emoji_category_scores = functions.calculate_emoji_category_scores(df)

        # Create a bar plot for emoji categories and scores
        st.title("Emoji Category Analysis")
        fig, ax = plt.subplots()
        for category, score in emoji_category_scores.items():
            ax.bar(category, score)
        plt.xlabel("Emoji Categories")
        plt.ylabel("Scores")
        plt.xticks(rotation=45)
        st.pyplot(fig)



        


    
if uploaded_file is not None:
    # ... (Your existing code for data preprocessing)

    # Extract emojis from the messages
    df['emojis'] = df['message'].apply(lambda x: [char for char in x if char in emoji.EMOJI_DATA])

    # Classify emojis
    df['emoji_emotion'] = df['emojis'].apply(functions.classify_emojis)

    # Translate and classify emotions for sentences
    df['sentence_emotion'] = functions.translate_and_classify_emotion(df['message'])

    # Calculate final scores
    df = functions.calculate_final_scores(df)

    # ... (Your existing code for displaying statistics and visualizations)

    # Plot emotion scores
    st.title("Emotion Scores")
    emotion_scores = df.groupby('sentence_emotion')['total_score'].mean()
    # Create a bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(emotion_scores.index, emotion_scores.values,color='pink')
    plt.xlabel('Emotion')
    plt.ylabel('Scores')
    plt.title('Emotion Scores')

    # Display the graph in Streamlit
    st.pyplot(plt)

    
plt.savefig('plot.svg', format='svg')
        
    
    
    




        





        


