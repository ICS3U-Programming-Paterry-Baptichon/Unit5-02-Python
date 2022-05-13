# Created by Paterry Baptichon
# Created on 2022-05-10
# this program calculates the area of a triangle

def caculate_area(base, height):
    # calculate area of triangle

    # the calculation of the the aera of a triangle 
    area = 1/2 * base * height

    # display the area of a triangle to the user
    print("The area of triangle is {0} cm²".format(area))


def main():
    # the input of user for base and height
    base = input("Enter the base of triangle (integer): ")
    height = input("Enter the height of triangle (integer): ")

    # call functions
    try:
        integer_as_base = int(base)
        integer_as_height = int(height)
        caculate_area(integer_as_base, integer_as_height)
    except Exception:
        print("It is not an integer")


if __name__ == "__main__":
    main()