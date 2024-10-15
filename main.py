import shutil
import os
import pathlib
from src.block_markdown import *

def main():
    copy("./static", "./public")

    generate_page("./content/index.md", "template.html", "./public/index.html")

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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    f = open(from_path, "r")
    md_content = f.read()
    f.close()

    f = open(template_path, "r")
    template = f.read()
    f.close()

    html = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)

    template = template.replace("{{ Content }}", html)
    template = template.replace("{{ Title }}", title)

    # write resulting html to file in public
    f = open(dest_path, "x")
    f.write(template)
    f.close()



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