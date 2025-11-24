import json


def extract_notebook(path):
    with open(path,'r',encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb["cells"]

    markdown_cells = []
    code_cells = []

    for cell in cells:
        if cell["cell_type"] == "code":
            code_cells.append("".join(cell["source"]))
        elif cell["cell_type"] == "markdown":
            markdown_cells.append("".join(cell["source"]))
    return {
        "code" : code_cells,
        "markdown" : markdown_cells
    }
# print(extract_notebook("early_stopping.ipynb"))


def prepare_text_for_llm(content):
    text = ""

    text += "### CODE CELLS:\n"
    for code in content["code"]:
        text += code + "\n\n"

    text += "### MARKDOWN CELLS:\n"
    for md in content["markdown"]:
        text += md + "\n\n"

    return text


extracted = extract_notebook("early_stopping.ipynb")
new_text = prepare_text_for_llm(extracted)

# print(new_text[:100])
print(new_text[1600:])