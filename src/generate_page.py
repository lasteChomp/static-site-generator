from block_markdown import markdown_to_html_node


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n\n")
    title = ""
    for line in lines:
        if line.startswith("# "):
            title += line[2:].strip()
            break
    return title

def generate_page(from_path: str, template_path: str, dest_path: str) -> str:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    try:
        with open(from_path, "r") as f:
            source_contents = f.read()
        with open(template_path, "r") as f:
            template_contents = f.read()
        source_contents_html = markdown_to_html_node(source_contents).to_html()
        source_contents_title = extract_title(source_contents)
        complete_html = template_contents.replace("{{ Title }}", source_contents_title).replace("{{ Content }}", source_contents_html)
        with open(dest_path, "w") as f:
            f.write(complete_html)
        return f"Generated page successfully from {from_path} to {dest_path} using {template_path}"
    except FileNotFoundError as error:
        return f"File not found: {error.filename}"
    