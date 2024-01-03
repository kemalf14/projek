import tkinter as tk
from tkinter.filedialog import asksaveasfile
from typing import Tuple, Callable
TINY_FONT = ('Lucida Console', 8)
SMALL_FONT = ('CalibriLight', 10)
MEDIUM_FONT = ('CalibriLight', 12)
LARGE_FONT = ('Lucida Bright', 20)
class StickyWindow:
    def __init__(
        self,
        name: str,
        colour: str,
        parent: tk.Tk,
        get_size: Callable[[], Tuple[int, int]],
    ) -> None:
        # function invoked when you click the create button ont the main frame
        self.new_window = tk.Toplevel(parent)
        if name == '':
            name = 'Untitled'
        self.name = name
        self.new_window.wm_title(name)
        top_note_frame = tk.LabelFrame(
            self.new_window, bg='#ffffff', font=SMALL_FONT,
        )
        save_button = tk.Button(top_note_frame, text='Save', command=self.save_file)
        save_button.pack(pady=5, expand=True, side=tk.LEFT)
        hide_button = tk.Button(top_note_frame, text='Hide', command=self.hide_sticky)
        hide_button.pack(pady=5, expand=True, side=tk.LEFT)
        show_button = tk.Button(top_note_frame, text='Show', command=self.show_sticky)
        show_button.pack(pady=5, expand=True, side=tk.LEFT)
        top_note_frame.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.get_size = get_size
        width, height = get_size()
        self.new_window.geometry(f'{width}x{height}')
        self.T = T = tk.Text(self.new_window, height=20, width=40, bg=colour)
        T.pack()
        T.configure(font='Calibri')
    def save_file(self) -> None:
        txt_content = self.T.get('1.0', 'end-1c')
        f = asksaveasfile(
            initialfile=self.name,
            defaultextension='.txt',
            filetypes=(
                ('Text Documents', '*.txt'),
                ('All Files', '*.*'),
            ),
        )
        if f is not None:
            f.write(txt_content)
            self.new_window.destroy()
    def show_sticky(self) -> None:
        width, height = self.get_size()
        self.new_window.geometry(f'{width}x{height}')
    def hide_sticky(self) -> None:
        self.new_window.geometry('0x50')
class SettingsWindow:
    def __init__(self, parent: tk.Tk):
        self.window = tk.Toplevel(parent)
        self.window.wm_title('Settings')
        settings_frame = tk.LabelFrame(
            self.window, bg='#ffffff', text='Settings', font=MEDIUM_FONT,
        )
        file_type_label = tk.Label(
            settings_frame, bg='#ffffff', text='Set default file save type:'
        )
        default_type = tk.StringVar
        file_type_entry = tk.Entry(
            settings_frame, bg='#ffffff', textvariable=default_type,
        )
        file_type_label.pack(padx=10, pady=10)
        file_type_entry.pack(padx=10, pady=10)
        save_settings = tk.Button(settings_frame, text='Save Settings')
        save_settings.pack(padx=10, pady=10)
        settings_frame.pack(fill=tk.BOTH, padx=10, pady=10)
class MyApp:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title(string='Stickies')
        self.window.attributes('-alpha', 0.95)
        self.window.configure(bg='#ffffff')
        self.mainloop = self.window.mainloop
        width, height = self.getscreensize_fraction(0.3, 0.5)
        self.window.geometry(f'{width}x{height}+{width+70}+10')
        frame = tk.LabelFrame(
            self.window, text='Stickies', bg='#ffffff', font=MEDIUM_FONT,
        )
        frame_name = tk.LabelFrame(
            frame, text='Name your note', bg='#ffffff', font=MEDIUM_FONT,
        )
        frame_colors = tk.LabelFrame(
            frame, text='Colors', bg='#ffffff', font=MEDIUM_FONT,
        )
        self.name_entry = tk.StringVar()
        name_entry = tk.Entry(
            frame_name, textvariable=self.name_entry, font=SMALL_FONT, bg='#f1f1f1',
        )
        self.purple = tk.StringVar()
        self.blue = tk.StringVar()
        self.orange = tk.StringVar()
        self.green = tk.StringVar()
        self.yellow = tk.StringVar()
        self.pink = tk.StringVar()
        color1 = tk.Checkbutton(
            frame_colors, text='Purple', bg='#dbcdf0', variable=self.purple, font=SMALL_FONT,
        )
        color1.deselect()
        color2 = tk.Checkbutton(
            frame_colors, text='Green', bg='#d0f4de', variable=self.green, font=SMALL_FONT,
        )
        color2.deselect()
        color3 = tk.Checkbutton(
            frame_colors, text='Blue', bg='#c6def1', variable=self.blue, font=SMALL_FONT,
        )
        color3.deselect()
        color4 = tk.Checkbutton(
            frame_colors, text='Pink', bg='#f2c6de', variable=self.pink, font=SMALL_FONT,
        )
        color4.deselect()
        color5 = tk.Checkbutton(
            frame_colors, text='Orange', bg='#f7d9c4', variable=self.orange, font=SMALL_FONT,
        )
        color5.deselect()
        color6 = tk.Checkbutton(
            frame_colors, text='Yellow', bg='#fcf6bd', variable=self.yellow, font=SMALL_FONT,
        )
        color6.deselect()
        # --PACK ELEMENTs----------------------------------------------------------------
        color1.pack(padx=5, pady=5)
        color2.pack(padx=5, pady=5)
        color3.pack(padx=5, pady=5)
        color4.pack(padx=5, pady=5)
        color5.pack(padx=5, pady=5)
        color6.pack(padx=5, pady=5)
        frame_name.pack(padx=10, pady=10, fill=tk.BOTH)
        name_entry.pack(padx=5, pady=5)
        frame.pack(expand=False, fill=tk.BOTH, padx=10, pady=10)
        frame_colors.pack(expand=False, fill=tk.BOTH, padx=10, pady=10)
        # Tells the program to return to the create sticky function on click
        my_create_button = tk.Button(
            frame, text='Create', command=self.create_sticky, font=SMALL_FONT,
        )
        my_create_button.pack(padx=5, pady=5)
        settings_button = tk.Button(
            frame, text='Settings', font=SMALL_FONT, command=self.open_settings,
        )
        settings_button.pack(padx=5, pady=10, side=tk.BOTTOM)
    @property
    def colour(self) -> str:
        if self.orange.get() == '1':
            return '#f7d9c4'
        if self.blue.get() == '1':
            return '#c6def1'
        if self.purple.get() == '1':
            return '#dbcdf0'
        if self.green.get() == '1':
            return '#d0f4de'
        if self.yellow.get() == '1':
            return '#fcf6bd'
        if self.pink.get() == '1':
            return '#f2c6de'
        return '#FFFFFF'
    def open_settings(self) -> None:
        SettingsWindow(parent=self.window)
    def getscreensize_fraction(self, fx: float = 0.3, fy: float = 0.3) -> Tuple[int, int]:
        return (
            int(fx*self.window.winfo_screenwidth()),
            int(fy*self.window.winfo_screenheight()),
        )
    def create_sticky(self) -> None:
        StickyWindow(
            name=self.name_entry.get(), colour=self.colour, parent=self.window,
            get_size=self.getscreensize_fraction,
        )
if __name__ == '__main__':
    MyApp().mainloop()