# Image Editor with OpenCV

This is a simple Python project that allows users to perform basic
editing operations on an image using **OpenCV**. The program is
interactive and works directly from the terminal, letting the user
choose actions such as drawing shapes, adding text, and saving the
edited image.

## Features

-   **Draw a Line** → Specify two points, color, and thickness to draw a
    line.\
-   **Draw a Circle** → Choose the center, radius, color, and
    thickness.\
-   **Draw a Rectangle** → Input two corner points, color, and
    thickness.\
-   **Add Text** → Write custom text on the image with adjustable
    position, font scale, color, and thickness.\
-   **Save Edited Image** → Option to save the modified image in a
    format of your choice.\
-   **Exit Anytime** → Clean exit from the program when done.

## Requirements

-   Python 3.x\
-   OpenCV (`cv2`)

Install OpenCV with:

``` bash
pip install opencv-python
```

## How to Run

1.  Clone this repository or download the script.\

2.  Open a terminal in the project folder.\

3.  Run the script:

    ``` bash
    python assignment2.py
    ```

4.  Enter your username when prompted.\

5.  Provide the path of the image you want to edit.\

6.  Follow the menu options to perform edits.

## Example Usage

    Enter Username: Rahul
    imput an image: sample.jpg

    What do you want to do Rahul ?
            1. Draw a Line?
            2. Draw a Circle?
            3. Draw a Rectangle?
            4. Add some text?
            5. Exit

After editing, you'll be asked:

    Rahul do you want to save the image? (Y/N)

If **Y**, you can specify the name and format, e.g.:

    name: edited_image
    format: png

Saved successfully as `edited_image.png`.
