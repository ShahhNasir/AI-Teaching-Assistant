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
print(extract_notebook("early_stopping.ipynb"))