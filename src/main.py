import os
from copy_static import copy_static_to_public
from generate_page import generate_pages_recursive

source_path = "./static"
destination_path = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copying_operation = copy_static_to_public(source_path, destination_path)
    generate_pages_recursive(dir_path_content, template_path, destination_path)
    print(copying_operation)

main()