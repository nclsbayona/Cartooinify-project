from tkinter import filedialog, Tk

def getImageLocation() -> str:
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"), ("all files", "*")))
    return root.filename

if __name__ == "__main__":
    print (getImageLocation())