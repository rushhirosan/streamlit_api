import youtubedata_app
import googletrend_app
import tweepy_app
import spotipy_app
import streamlit as st

# Static pages
PAGES = {
    "youtube data api": youtubedata_app,
    "google trend api": googletrend_app,
    "twitter api": tweepy_app,
    "spotify api": spotipy_app
}


def main():
    """
    Main app
    """
    st.sidebar.title('API experiments')
    st.sidebar.markdown(
        """
        ## This site is to experiment well-known APIs :wink:
        """)

    # Sidebar body
    selection = st.sidebar.radio("Open up", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

    # Layout adjustment
    st.sidebar.write('\n')
    st.sidebar.write('\n')

    # Brief explanation
    st.sidebar.info(
        """
        * Thru Youtube data api, 
        you will be able to search video trend and by query.\n
        * Thru twitter api, 
        you will be able to search trend and by query.\n
        * Thru gtrend api, 
        you will be able to grab what's in keyword trend.\n
        * Thru spotify api, 
        you will be able to grab what's in trending podcast.\n
        More to come..
        """
    )


if __name__ == "__main__":
    main()