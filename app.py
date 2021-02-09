import streamlit as st

import utils.display as udisp

import src.pages.home
    


MENU = {
    "Home" : src.pages.home,
}

def main():
    menu = MENU["Home"]
    udisp.render_page(menu)



if __name__ == "__main__":
    main()