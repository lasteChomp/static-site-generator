from copy_static import copy_static_to_public


def main():
    source_path = "./static"
    destination_path = "./public"
    copying_operation = copy_static_to_public(source_path, destination_path)
    print(copying_operation)

main()