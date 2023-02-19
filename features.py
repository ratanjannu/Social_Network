from network import Network


class Recommendation(Network):
    """
           This class inherits from the Network class and overwrites its abstract methods.
           The Network class is the parent class for this.
           This class has multiple features which fulfils the requirements of the network:-
               1. Recommend friends to a user
               2. Display the number of friends a user has
               3. Display the member with the least or 0 friends in the social network
               4. Display the relationships of a member
               5. The main function calling all the functions and asking the user to choose a feature to access
               6. Switch cases for the user choices
               7. Finding all the indirect relationships present in the social network


           Important methods used:

           recommend_friend(): This method recommends a friend to a member the user wants by using common_friends

           get_friends(): This method displays all the friends a member has

           least_friends(): It displays the member with the least or 0 friends in the social network

           member_relationships(): Used to display the relationships of a given member has in the network

           indirect_relationships(): It shows the friend of a friend and all the indirect relationships that are present in the social network

           main(): It is used to call all the functions and gives the user the option to choose which feature they would like to access

           user_choices(): It has a switch case of choices in the form of if elif conditionals and depending on the users choice it is used to run the methods and takes in a choice parameter

           Notable instance attributes used:

           __common_friends (2d list of int): Matrix of the order 2*2 containing the number of common friends between the members

           __indirect_friends (dict): It is a dictionary consisting of the friends of a friend

    """

    def __init__(self):
        super().__init__()
        self.common_friends = self.find_common_friends()

    # It displays the recommended friend for a given user
    def recommend_friend(self):

        member_id = int(input("Enter the member id of the person you would like to recommend a friend to? : "))

        most_likely_friend = None
        max_common_friends = 0

        # Loops through the indices and the values using enumerate function
        for i, member in enumerate(self.social_NW.keys()):
            # If the value is the member or already is the member's friend it passes
            if i == member_id or member in self.social_NW[member_id]:
                continue
            # Checks if the user has atleast 1 friend and recommends a new friend
            if self.common_friends[member_id][i] > max_common_friends:
                max_common_friends = self.common_friends[member_id][i]
                most_likely_friend = member
                print(f"The recommended friend for {member_id} is : {most_likely_friend}")
        return most_likely_friend

    # It displays the friends a user has
    def get_friends(self):
        member_info = input("Enter the member name or member ID to display their friends: ")
        member_info_int = int(member_info)
        if member_info.isdigit():
            if member_info_int in self.social_NW.keys():
                print(f"Number of friends for member {member_info_int} : {len(self.social_NW[member_info_int])}")

            else:
                print("Not found")

        else:
            for member in self.social_NW.keys():
                if member == member_info:
                    print(f"Number of friends for member {member_info} : {len(self.social_NW[member_info])}")

                else:
                    print("Not found")

    # It displays the member with the least or 0 friends in the social network
    def least_friends(self):
        member_friends = [(member, len(friends)) for member, friends in self.social_NW.items()]
        min_friends = min(member_friends, key=lambda x: x[1])[1]
        least_friends = [member for member, friends in member_friends if friends == min_friends or friends == 0]
        print("Members with the least number of friends: ")
        for member in least_friends:
            print(f"{member}")

    def zero_friends(self):
        count = 0
        for member in self.social_NW.keys():
            if len(self.social_NW[member]) == 0:
                print(f"{member} has 0 friends")
                count += 1

        if count == 0:
            print("No member has 0 friends")

    # Used to display the relationships of a given member has in the network
    def member_relationships(self):

        member_info = input("Enter the member info to check their relationships: ")
        member_info_int = int(member_info)

        if member_info_int in self.social_NW.keys():
            friends = self.social_NW[member_info_int]
            print(f"{member_info} is friends with: {friends}")
        else:
            print(f"{member_info} not found in the member list")

    # It shows the friend of a friend and all the indirect relationships that are present in the social network
    def indirect_relationships(self):

        indirect_friends = {}
        for user in self.social_NW:
            indirect_friends[user] = []
            for friend in self.social_NW[user]:
                for indirect_friend in self.social_NW[friend]:
                    if indirect_friend == user:
                        continue
                    if indirect_friend not in indirect_friends[user]:
                        indirect_friends[user].append(indirect_friend)

        for member, friends in indirect_friends.items():
            print(f"{member} -> {friends}")

    def main(self):
        while True:

            print("1 | Initiate and display social network\n"
                  "2 | Display common friend\n"
                  "3 | Recommend friend for a member of the network\n"
                  "4 | Display number of friends for a member of your choice\n"
                  "5 | Display the user with least or no friends\n"
                  "6 | Display relationships for a member\n"
                  "7 | Display all the indirect relationships in the social network\n"
                  "8 | Initiate new social network\n"
                  "9 | Display member with zero friends\n"
                  "n | Exit\n")

            choice = self.user_choices(input("What would you like to do: ").lower())

            if choice == 1:
                return False
            else:
                return True

    # It has a switch case of choices in the form of if elif conditionals and depending on the users choice it is used to run the methods and takes in a choice parameter
    def user_choices(self, choice):
        while True:

            if choice == "1":
                self.create_network()
                self.validate_input()
                return 1
            elif choice == "2":
                self.display_common_friends()
                return 1
            elif choice == "3":
                self.recommend_friend()
                return 1
            elif choice == "4":
                self.get_friends()
                return 1
            elif choice == "5":
                self.least_friends()
                return 1
            elif choice == "6":
                self.member_relationships()
                return 1
            elif choice == "7":
                self.indirect_relationships()
                return 1
            elif choice == "8":
                return 0
            elif choice == "9":
                self.zero_friends()
                return 1
            elif choice == "n":
                print("Thank you! See you again :)")
                return exit()
            else:
                print("Invalid input!")
                return 0
