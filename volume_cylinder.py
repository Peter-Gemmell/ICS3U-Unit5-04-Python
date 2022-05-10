#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on May 2022
# This program calculates volume cylinder using function

import math


def volume_cylinder(radius, height):
    # this function calculates volume of cylinder

    # calculation
    volume = math.pi * (radius**2) * height

    # output
    return volume


def main():
    # gets input from user & outputs volume

    # inputs
    radius_string = input("Enter the radius of cylinder in cm : ")
    height_string = input("Enter the height of cylinder in cm : ")

    try:
        radius_user = float(radius_string)
        height_user = float(height_string)
        volume_cylinderd_rounded = round(volume_cylinder(radius_user, height_user), 2)
        print(
            "The volume of the cylinder with a radius of {}"
            " and height of {} is {} cm³.".format(
                radius_user, height_user, volume_cylinderd_rounded
            )
        )

    except Exception:
        print("Invalid input, please try again.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
