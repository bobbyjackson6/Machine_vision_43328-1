<<<<<<< HEAD
import cv2.aruco as aruco
import cv2

def generate_marker( save_img_name ):
    # Select type of aruco marker (size)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_1000)

    # Create an image from the marker
    # second param is ID number
    # last param is total image size
    img = aruco.drawMarker(aruco_dict, 2, 700)
    cv2.imwrite(save_img_name, img)

    # Display the image to us
    cv2.imshow('frame', img)
    # Exit on any key
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def generate_board( save_img_name ):
    # Create gridboard, which is a set of Aruco markers
    # the following call gets a board of markers 5 wide X 7 tall
    gridboard = aruco.GridBoard_create(
        markersX=5,
        markersY=7,
        markerLength=0.04,
        markerSeparation=0.01,
        dictionary=aruco.Dictionary_get(aruco.DICT_5X5_1000))

    # Create an image from the gridboard
    img = gridboard.draw(outSize=(988, 1400))
    cv2.imwrite( save_img_name, img)

    # Display the image to us
    cv2.imshow('Gridboard', img)
    # Exit on any key
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def generate_chess_board( save_img_name ):
    # Create ChArUco board, which is a set of Aruco markers in a chessboard setting
    # meant for calibration
    # the following call gets a ChArUco board of tiles 5 wide X 7 tall
    gridboard = aruco.CharucoBoard_create(
        squaresX=5,
        squaresY=7,
        squareLength=0.04,
        markerLength=0.02,
        dictionary=aruco.Dictionary_get(aruco.DICT_5X5_1000))

    # Create an image from the gridboard
    img = gridboard.draw(outSize=(988, 1400))
    cv2.imwrite("test_charuco.jpg", img)

    # Display the image to us
    cv2.imshow('Gridboard', img)
    # Exit on any key
    cv2.waitKey(0)
=======
import cv2.aruco as aruco
import cv2

def generate_marker( save_img_name ):
    # Select type of aruco marker (size)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_1000)

    # Create an image from the marker
    # second param is ID number
    # last param is total image size
    img = aruco.drawMarker(aruco_dict, 2, 700)
    cv2.imwrite(save_img_name, img)

    # Display the image to us
    cv2.imshow('frame', img)
    # Exit on any key
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def generate_board( save_img_name ):
    # Create gridboard, which is a set of Aruco markers
    # the following call gets a board of markers 5 wide X 7 tall
    gridboard = aruco.GridBoard_create(
        markersX=5,
        markersY=7,
        markerLength=0.04,
        markerSeparation=0.01,
        dictionary=aruco.Dictionary_get(aruco.DICT_5X5_1000))

    # Create an image from the gridboard
    img = gridboard.draw(outSize=(988, 1400))
    cv2.imwrite( save_img_name, img)

    # Display the image to us
    cv2.imshow('Gridboard', img)
    # Exit on any key
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def generate_chess_board( save_img_name ):
    # Create ChArUco board, which is a set of Aruco markers in a chessboard setting
    # meant for calibration
    # the following call gets a ChArUco board of tiles 5 wide X 7 tall
    gridboard = aruco.CharucoBoard_create(
        squaresX=5,
        squaresY=7,
        squareLength=0.04,
        markerLength=0.02,
        dictionary=aruco.Dictionary_get(aruco.DICT_5X5_1000))

    # Create an image from the gridboard
    img = gridboard.draw(outSize=(988, 1400))
    cv2.imwrite("test_charuco.jpg", img)

    # Display the image to us
    cv2.imshow('Gridboard', img)
    # Exit on any key
    cv2.waitKey(0)
>>>>>>> 42a659055a6d57bad3c490d3d672ed9f2327a43b
    cv2.destroyAllWindows()