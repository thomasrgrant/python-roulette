# Create Folders
import os

class Folders:
    directory_names = [
        "images",
        "images/numbers",
        "images/profile",
        "images/choice",
        "images/search",
        "images/table",
        
        "data",
        "numdata",
        "numdata/saved_spins",
        "numdata/saved_spins/random",
        "numdata/saved_spins/bv",
        "numdata/stats_data",
        "numdata/stats_data/random",
        "numdata/stats_data/bv"
    ]

    @staticmethod
    def create_directories():
        for dir_name in Folders.directory_names:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
                # print("Directory", dir_name, "created")
            # else:
            #     print("Directory", dir_name, "already exists")

# Create Folders
Folders.create_directories()
