import nbformat
import os

print(os.getcwd())

def update_tags_in_notebook(notebook_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, nbformat.NO_CONVERT)

    # Iterate through the cells
    for cell in notebook.cells:
        # Remove 'hide-cell' tag if it exists
        print(cell.get('metadata', {}).get('tags', []))
        if 'hide-cell' in cell.get('metadata', {}).get('tags', []):
            print('Removing hide-cell tag from cell')
            cell.metadata['tags'].remove('hide-cell')

        # Check if the cell is a code cell
        if cell.cell_type == 'code':
            # Count the number of lines in the code
            code_lines = cell.source.splitlines()
            if len(code_lines) > 20:
                # Add the 'hide-input' tag if it doesn't already exist
                if 'hide-input' not in cell.metadata.get('tags', []):
                    if 'tags' not in cell.metadata:
                        cell.metadata['tags'] = []
                    cell.metadata['tags'].append('hide-input')
                    print('Adding hide-input tag to cell')

    # Save the modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

# Example usage
notebook_path = 'Website/main/analysis.ipynb'  # Replace with your notebook path
update_tags_in_notebook(notebook_path)
