import streamlit as st
import preprocessor, functions
import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.title("whatapp chat analyzer")

uploaded_file = st.sidebar.file_uploader("choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    

    #fetch unique users

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"overall")

    selected_user = st.sidebar.selectbox("show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words, num_media_messages, links = functions.fetch_stats(selected_user,df)

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
            st.header("Linkes Shared")
            st.title(links)

        #monthly timeline
        st.title("Monthly TimeLine")
        timeline = functions.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'],timeline['message'], color='green')
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)

        #daily timeline
        st.title("daily TimeLine")
        timeline = functions.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['Date'],timeline['message'], color='black')
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)
        st.dataframe(timeline)

        #activity map
        st.title("Activity Map")
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = functions.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values,color='green')
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)


        with col2:
            st.header("Most busy month")
            busy_month = functions.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)


        #activity heatmap
        st.title("Weekly Activity")
        user_heatmap = functions.activity_heatmap(selected_user,df)
        fig, ax=plt.subplots()
        ax=sns.heatmap(user_heatmap)
        st.pyplot(fig)


        #finding the busiest users in the group(group level)
        if selected_user =='overall':
            st.title('Most Busy Users')
            x, new_df = functions.most_busy_users(df)
            fig, ax = plt.subplots()

            col1,col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='blue')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            
            with col2:
                st.dataframe(new_df)

        #wordcloud
        st.title("Word Cloud")
        df_wc = functions.create_wordcloud(selected_user,df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        #most common words
        
        most_common_df = functions.most_common_words(selected_user, df)

        fig, ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1], color='magenta')
        plt.xticks(rotation= 'vertical')
        st.title("Most Common Words and emojis")
        st.pyplot(fig)
        st.dataframe(most_common_df)


        


