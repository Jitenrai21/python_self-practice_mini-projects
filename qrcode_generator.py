import qrcode as qr
from PIL import Image
img = qr.make('https://github.com/Jitenrai21/AI_MazeSolver_by_SearchAlgorithms/blob/main/AI_midterm/maze_solving.py')
img.save("gitqr.png")

# The above commented code creates and saves a qr in the file containing folder for the given url.

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )

# qr.add_data("https://github.com/Jitenrai21/AI_MazeSolver_by_SearchAlgorithms/blob/main/AI_midterm/maze_solving.py")
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")

# img.save('gitqr.png')