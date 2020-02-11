# import libraries
import streamlit as st
from screens import home, screen_1, screen_2, screen_3, screen_4


# main function
def main():
    """

    :return:
    """

    # Dashboard Title
    st.title("MY DASHBOARD")

    # create select box on sidebar
    activities = ['Home', 'Screen 1', 'Screen 2', 'Screen 3', 'Screen 4']
    selected_screen = st.sidebar.selectbox("Select Screen", activities)

    # render screens
    if selected_screen == "Home":
        st.sidebar.markdown('---')
        st.markdown("hello")
    elif selected_screen == "Screen 1":
        screen_1.render()
    elif selected_screen == "Screen 2":
        screen_2.render()
    elif selected_screen == "Screen 3":
        screen_3.render()
    elif selected_screen == "Screen 4":
        screen_4.render()

    # about on side bar
    st.sidebar.markdown("---")
    st.sidebar.markdown("# About \n This app has been developed by [Pavan] (https://github.com/pavancs) \
     using [Streamlit](https://streamlit.io/).")


if __name__ == '__main__':
    main()
