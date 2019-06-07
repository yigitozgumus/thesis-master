import os
from contextlib import contextmanager
from shutil import copytree, rmtree


@contextmanager
def working_directory(directory):
    owd = os.getcwd()
    try:
        os.chdir(directory)
        yield directory
    finally:
        os.chdir(owd)


def backup():
    thesis_path = "/Users/yigitozgumus/Google Drive/THESIS/"
    thesis_dir = "Thesis_Document"
    backup_path_1 = "/Users/yigitozgumus/Documents"
    backup_path_2 = "/Users/yigitozgumus/Dropbox"
    backup_dir = "Thesis_backup"
    # Delete the old backup
    with working_directory(backup_path_1):
        if os.path.exists(backup_dir):
            print("Cleaning old Backup from {}".format(backup_path_1))
            rmtree(backup_dir)
    with working_directory(backup_path_2):
        if os.path.exists(backup_dir):
            print("Cleaning old Backup from {}".format(backup_path_2))
            rmtree(backup_dir)
    # Backup the Thesis
    with working_directory(thesis_path):
        copytree(thesis_dir, os.path.join(backup_path_1, backup_dir))
        copytree(thesis_dir, os.path.join(backup_path_2, backup_dir))
        print("Backup is Completed")


def main():
    backup()


if __name__ == "__main__":
    main()
