from gui.main_window import create_main_window


if __name__ == "__main__":
    main_window = create_main_window()
    print(main_window.children)
    main_window.mainloop()
