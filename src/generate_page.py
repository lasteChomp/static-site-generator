import os
from block_markdown import markdown_to_html_node


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("no title found")

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> str:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    try:
        with open(from_path, "r") as f:
            source_contents = f.read()
        with open(template_path, "r") as f:
            template_contents = f.read()
        source_contents_html = markdown_to_html_node(source_contents).to_html()
        source_contents_title = extract_title(source_contents)
        complete_html = template_contents.replace("{{ Title }}", source_contents_title).replace("{{ Content }}", source_contents_html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
        dest_dir_path = os.path.dirname(dest_path)
        if dest_dir_path != "":
            os.makedirs(dest_dir_path, exist_ok=True)
        with open(dest_path, "w") as f:
            f.write(complete_html)
        return f"Generated page successfully from {from_path} to {dest_path} using {template_path}"
    except FileNotFoundError as error:
        return f"File not found: {error.filename}"
    except ValueError as error:
        return f"{error}"


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str):
    dir_path_contents = os.listdir(dir_path_content)
    for path in dir_path_contents:
        dir_path_contents_path = os.path.join(dir_path_content, path)
        dest_dir_path_contents = os.path.join(dest_dir_path, path)
        if os.path.isfile(dir_path_contents_path) and dir_path_contents_path.endswith(".md"):
            dest_dir_path_contents = dest_dir_path_contents.replace(".md", ".html")
            generate_page(dir_path_contents_path, template_path, dest_dir_path_contents, basepath)
        if os.path.isdir(dir_path_contents_path):
            generate_pages_recursive(dir_path_contents_path, template_path, dest_dir_path_contents, basepath)
    