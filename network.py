from os.path import exists
import numpy


class Network:

    """
        This class is responsible for the initiation of the social network, it creates the network by asking for a valid file name, checks if the file exists and reads through it.
        It further creates a data structure to hold the social network in the form of a dictionary and populates it accordingly.

        With the help of an efficient and easy formula of o(n^2) complexity it calculates the common friends with the use of the intersection function


        Important methods used:

        create_network(): Handles the creation of the network from the given file directory, populates the data structure and allows the user to see the social network by pretty printing it

        validate_input(): It validates the input making sure there is no error in the data file provided and ensures consistency

        find_common_friends(): It parses relationships in the social_NW dictionary and stores them in the common_friends matrix created to store this data. The matrix thus returned
                                is later used in recommending friends and other methods.

        get_member_count(): It returns the value of the member count of the data file to allow easy re-usability for other methods

        display_common_friends(): It displays the common friends matrix

        Instance attributes:

        __social_NW (dict): Dictionary containing the relationships between members and friends, uses member_id

        __member_count( int): Contains the member count in the social network

        __common_friends (2d list of int): Matrix of the order 2*2 containing the number of common friends between the members

        __is_running (bool): Flag set to keep the while loop running

    """
    social_NW = {}
    is_running = True

    def __init__(self):
        self.__member_count = 0

    # creates the social network
    def create_network(self):

        while self.is_running:

            # Takes the name of the file as an input
            file_name = input("Enter the name of the data file: ")

            # Stops the process if the user wants to
            if file_name == "n":
                self.is_running = False
                break

            if exists(file_name):
                with open(file_name, 'r') as file:
                    self.__member_count = int(file.readline())

                    # Initiates the dictionary
                    for i in range(self.__member_count):
                        self.social_NW[i] = []

                    # Splits the members from the data file separated by a space, and strips them line by line
                    # count = 0
                    for line in file:
                        split_ids = line.split(" ")
                        new_ids = []

                        for split_id in split_ids:
                            new_ids.append(split_id.strip("\n"))

                        # Populates the dictionary with the members and friends
                        member = int(new_ids[0])

                        for user in new_ids:
                            friend = int(user)
                            if friend == member:
                                continue
                            if friend not in self.social_NW[member]:
                                self.social_NW[member].append(friend)
                            if member not in self.social_NW[friend]:
                                self.social_NW[friend].append(member)

                    print(self.social_NW)

            else:
                print("Error: Unable to open file. Please enter a valid file name.")

            # Asks the user if they want to display the social network
            display = input("Do you want to display the social network? (y/n): ").lower()

            # Pretty prints the social network
            if display == "y":
                for member, friends in self.social_NW.items():
                    print(f"{member} -> {friends}")

            self.is_running = False
            break

    # Validates the data in the data file to ensure consistency in the network
    def validate_input(self):
        for member in self.social_NW:
            for friend in self.social_NW[member]:
                if member not in self.social_NW[friend]:
                    raise Exception(f"Network is consistent, inconsistency is between {member} and {friend} ")
        print("Input is validated successfully")

    # Parses the relationships in the __social_NW to return a matrix of common friends between the members
    def find_common_friends(self):

        # Using numpy creates a 2D matrix using the dictionary for rows and columns
        common_friends = numpy.zeros((len(self.social_NW), len(self.social_NW)))

        # Looping through the members and their indices using enumerate function and finding the common friend
        # through the intersection function to help find the common friend
        for i, member1 in enumerate(self.social_NW.keys()):
            for j, member2 in enumerate(self.social_NW.keys()):
                if i == j:
                    common_friends[i, j] = len(set(self.social_NW[member1]).intersection(self.social_NW[member2]))
                elif i != j:
                    common_friends[i, j] = len(set(self.social_NW[member1]).intersection(self.social_NW[member2]))

        # Pretty prints the common friends of the social network
        # display_common_friends = input("Do you want to see the common friends?(y/n) :  ").lower()

        # if display_common_friends == "y":
        #     print(common_friends)
        self.common_friends = common_friends
        return common_friends

    # Displays the common friends matrix
    def display_common_friends(self):
        print(self.common_friends)

    # Returns the value of the number of members present in the social network
    @property
    def get_member_count(self):
        return self.__member_count


