import shutil
import os
import pathlib

def main():
    copy("./static", "./public")

def copy(src_path, dest_path):
    # make_public_test_dir()

    # base case
    if os.path.isfile(src_path):
        return

    src_paths = os.listdir(src_path)

    # delete all the contents of the dest directory
    delete_dir_contents(dest_path)

    # copy all files and directories and sub-directories to dest
    src_paths = os.listdir(src_path)
    for path in src_paths:
        src = os.path.join(src_path, path)
        dest = os.path.join(dest_path, path)
        print(f"Copying src: {src} to dest: {dest}")
        if os.path.isfile(src):
            shutil.copy(src, dest)
        else:
            os.mkdir(dest)

        #recursive call
        copy(src, dest)

    # log the path of each file that is copied (for debugging)

    # notes:
    #  -os.path.exists could be used to stop the recursion possibly
    #  -os.listdir gets me a list of the entries in the dir (files and sub-dirs)
    #  -os.path.join concatentates a path and all members of paths (is the return a str or a list of strs?)
    #  -os.path.isfile returns true if path is a file
    #  -os.mkdir makes new directory but won't overwrite existing directory (and will throw FileExistsError)
    #  -shutil.copy copies a src file to a file or directory dst
    #  -shutil.rmtree delete an entire directory tree

def make_public_test_dir():
    pathlib.Path("./public/test/test").mkdir(parents=True)
    
    if os.path.exists("./public"):
        f = open("./public/test.txt", "x")
        f.close()

def delete_dir_contents(path):
    public_sub_dirs = os.listdir(path)
    for dir in public_sub_dirs:
        path_to_delete = os.path.join(path, dir)
        if os.path.isfile(path_to_delete):
            os.remove(path_to_delete)
        else:
            shutil.rmtree(path_to_delete)

main()