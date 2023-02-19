
"""
    Author: Ratan Rohidas Jannu
    StudentID: 001236905

    This class is responsible for managing all the methods and running all the fuctions created
    other classes it has a main() method which runs it.
    METHODS:
        main()

    INSTANCE ATTRIBUTES:
        social_network:
        should_exit:
"""

import features
import ASCII_ART


def main():
    print(ASCII_ART.header)
    print(ASCII_ART.home_screen)
    while True:
        social_network = features.Recommendation()
        should_exit = social_network.main()
        if should_exit:
            return


if __name__ == "__main__":
    main()
