import os
from copy_static import copy_static_to_public
from generate_page import generate_page

source_path = "./static"
destination_path = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copying_operation = copy_static_to_public(source_path, destination_path)
    generating_page_operation = generate_page(
        os.path.join(dir_path_content, "index.md"), 
        template_path, 
        os.path.join(destination_path, "index.html"),
    )
    print(copying_operation)
    print(generating_page_operation)

main()