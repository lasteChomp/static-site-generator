from copy_static import copy_static_to_public
from generate_page import generate_page


def main():
    source_path = "./static"
    destination_path = "./public"
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./public/index.html"
    copying_operation = copy_static_to_public(source_path, destination_path)
    generating_page_operation = generate_page(from_path, template_path, dest_path)
    print(copying_operation)
    print(generating_page_operation)

main()