import sys
from copy_static import copy_static_to_public
from generate_page import generate_pages_recursive


if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"
source_path = "./static"
destination_path = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copying_operation = copy_static_to_public(source_path, destination_path)
    generate_pages_recursive(dir_path_content, template_path, destination_path, basepath)
    print(copying_operation)

main()