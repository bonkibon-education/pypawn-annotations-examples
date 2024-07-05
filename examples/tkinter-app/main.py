from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from pypawn_annotations import Annotation, PawnFunction, FUNC_TITLES


class App(Tk):
    def __init__(self):
        super().__init__()

        # app settings
        self.title('pypawn-auto-annotation')
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # pre_cache: icons
        self._icons = {
            "copy_disabled": PhotoImage(file="icons/icon_copy_disabled.png"),
            "copy_enabled": PhotoImage(file="icons/icon_copy_enabled.png"),
            "visibility_disabled": PhotoImage(file="icons/icon_visibility_disabled.png"),
            "visibility_enabled": PhotoImage(file="icons/icon_visibility_enabled.png"),
        }

        # pre_cache: scrollbar
        self._scrollbar_style = ttk.Style()
        self._scrollbar_style.theme_use("clam")
        self._scrollbar_style.configure(
            style="Horizontal.TScrollbar",
            background="#CECECE",
            troughcolor="#595B5D",
            arrowsize=15
        )

        # pre_cache: output buffer
        self._cache_split_lines: list = list()

        # draw: panels
        self._annotation_panel_input()
        self._annotation_panel_output()

    def _annotation_panel_input(self):
        # Frames in panel
        panel = Frame(master=self)
        body = Frame(master=panel)
        header = Frame(master=panel, bg="#3C3F41")
        body.setvar(name="variable:input", value=True)

        # Header: title
        Label(
            master=header,
            text="INPUT",
            font="Arial 14 bold",
            foreground="#ECBB06",
            bg="#3C3F41"
        ).pack(padx=120)

        # Header: button copy
        button_copy = Button(
            master=header,
            borderwidth=0,
            state="disabled",
            background="#3C3F41",
            activebackground="#3C3F41",
            activeforeground="#3C3F41",
            highlightcolor="#50C878",
            image=self._icons["copy_disabled"],
            command=lambda: self._on_copy_to_clipboard(text)
        )

        button_copy.place(x=-28, width=24, height=26, relx=1.0, rely=0.0, anchor="ne")

        # Header: button visibility body
        button_visibility = Button(
            master=header,
            borderwidth=0,
            background="#3C3F41",
            activebackground="#3C3F41",
            activeforeground="#3C3F41",
            highlightcolor="#50C878",
            image=self._icons["visibility_enabled"],
            command=lambda: self._switch_visibility_body(body, button_visibility, "variable:input")
        )

        button_visibility.place(width=24, relx=1.0, rely=0.0, anchor="ne")

        # Body: text
        text = Text(
            master=body,
            height=20,
            wrap="none",
            bg="#2B2B2B",
            foreground="white"
        )

        text.pack(fill=BOTH, expand=True)

        # Body: scrollbar
        scrollbar = ttk.Scrollbar(
            body,
            orient="horizontal",
            command=text.xview,
            style="Horizontal.TScrollbar"
        )

        text.config(xscrollcommand=scrollbar.set, insertbackground="white")
        scrollbar.pack(fill=X)

        # packing panel
        header.pack(fill=X, side=TOP)
        body.pack(fill=BOTH, expand=True)
        panel.pack(side=TOP, fill=BOTH, expand=True)

        # tags
        text.tag_config("error#highlight", foreground="red")
        text.tag_config("complete#highlight", foreground="#50C878")

        # event
        text.bind("<KeyRelease>", self._on_key_release)

        self.text_panel1 = text
        self.button_copy_panel1 = button_copy

    def _annotation_panel_output(self):
        # Frames in panel
        panel = Frame(master=self)
        body = Frame(master=panel)
        header = Frame(master=panel, bg="#3C3F41")
        body.setvar(name="variable:output", value=False)

        # Header: title
        Label(
            master=header,
            text="OUTPUT",
            font="Arial 14 bold",
            foreground="#50C878",
            bg="#3C3F41"
        ).pack()

        # Header: button copy
        button_copy = Button(
            master=header,
            borderwidth=0,
            state="disabled",
            background="#3C3F41",
            activebackground="#3C3F41",
            activeforeground="#3C3F41",
            highlightcolor="#50C878",
            image=self._icons["copy_disabled"],
            command=lambda: self._on_copy_to_clipboard(text)
        )

        button_copy.place(x=-28, width=24, height=26, relx=1.0, rely=0.0, anchor="ne")

        # Header: button visibility body
        button_visibility = Button(
            master=header,
            borderwidth=0,
            background="#3C3F41",
            activebackground="#3C3F41",
            activeforeground="#3C3F41",
            highlightcolor="#50C878",
            image=self._icons["visibility_disabled"],
            command=lambda: self._switch_visibility_body(body, button_visibility, "variable:output")
        )

        button_visibility.place(width=24, relx=1.0, rely=0.0, anchor="ne")

        # Body: text
        text = Text(
            master=body,
            height=20,
            wrap="none",
            bg="#2B2B2B",
            foreground="white"
        )

        text.pack(fill=BOTH, expand=True)

        # Body: scrollbar
        scrollbar = ttk.Scrollbar(
            body,
            orient="horizontal",
            command=text.xview,
            style="Horizontal.TScrollbar"
        )

        text.config(xscrollcommand=scrollbar.set, insertbackground="white")
        text.pack(fill=BOTH, expand=True)
        scrollbar.pack(fill=X)

        # packing panel
        header.pack(fill=X, side=TOP)
        panel.pack(side=TOP, fill=BOTH, expand=True)

        """ Events """
        # key release
        text.bind("<KeyRelease>", self._on_key_release)

        # block all key
        text.bind("<Key>", lambda e: "break")

        # allowed copy text
        text.bind("<Control-c>", self._on_hotkey_press)

        # allowed select all text
        text.bind("<Control-a>", self._on_hotkey_press)

        self.text_panel2 = text
        self.button_copy_panel2 = button_copy

    # Unblock hotkey press
    def _on_hotkey_press(self, e):
        pass

    def _on_copy_to_clipboard(self, widget):
        _text: str = widget.get(1.0, END).rstrip()

        if len(_text):
            self.clipboard_clear()
            self.clipboard_append(_text)
            showinfo(title="Information", message="Complete copy!")

    def _switch_visibility_body(self, widget, button, variable_name: str):
        value: any = widget.getvar(variable_name)

        if value:
            widget.pack_forget()
            widget.setvar(variable_name, value=False)
            button.config(image=self._icons["visibility_disabled"])
        else:
            widget.pack(fill=BOTH, expand=True)
            widget.setvar(variable_name, value=True)
            button.config(image=self._icons["visibility_enabled"])

    def _on_key_release(self, key):
        # change icon: button copy - panel1
        if key.char != " ":
            if len(self.text_panel1.get('1.0', END)) > 1:
                self.button_copy_panel1.config(state='normal', image=self._icons['copy_enabled'])
            else:
                self.button_copy_panel1.config(state='disable', image=self._icons['copy_disabled'])

        # filter key.char
        if not (key.char == " " or key.char == "\r"):
            return

        # split lines
        split_lines: list = self.text_panel1.get("1.0", END).splitlines()
        found_title_lines: list = [line for line in split_lines if line.split(' ')[0] in FUNC_TITLES]

        if not found_title_lines or found_title_lines == self._cache_split_lines:
            return

        # delete: highlight, lines
        self.text_panel1.tag_remove("highlight", "1.0", END)
        self.text_panel2.delete("1.0", END)

        # change icon: button copy - panel2
        self.button_copy_panel2.config(state='disable', image=self._icons['copy_disabled'])

        # caching
        self._cache_split_lines = found_title_lines

        for item in found_title_lines:
            function = PawnFunction(item)

            if function.flags():
                # Show annotation
                annotation = Annotation(description=function.name, function=function)
                self.text_panel2.insert(END, annotation.show() + "\n" + function.string + "\n\n")
                del annotation

                # Complete handling | Parse lines and set highlight
                for i, line in enumerate(split_lines):
                    if line in item: self.text_panel1.tag_add("complete#highlight", f"{i + 1}.0", f"{i + 1}.end")
            else:
                # Error handling | Parse lines and set highlight
                for i, line in enumerate(split_lines):
                    if line in item: self.text_panel1.tag_add("error#highlight", f"{i + 1}.0", f"{i + 1}.end")
                return

        # change icon
        if len(self.text_panel2.get('1.0', '1.1').rstrip()):
            self.button_copy_panel2.config(state='normal', image=self._icons['copy_enabled'])


if __name__ == "__main__":
    app = App()
    app.mainloop()
