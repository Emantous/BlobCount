from src.main import main


def test_image1():
    path = "test/images/1.png"
    number_of_objects = 7
    assert main(path)==number_of_objects


def test_image2():
    path = "test/images/2.png"
    number_of_objects = 4
    assert main(path)==number_of_objects


def test_image3():
    path = "test/images/3.png"
    number_of_objects = 3
    assert main(path)==number_of_objects


def test_image4():
    path = "test/images/4.png"
    number_of_objects = 9
    assert main(path)==number_of_objects


def test_image5():
    path = "test/images/5.png"
    number_of_objects = 9
    assert main(path)==number_of_objects


def test_blank():
    path = "test/images/blank.png"
    number_of_objects = 0
    assert main(path)==number_of_objects