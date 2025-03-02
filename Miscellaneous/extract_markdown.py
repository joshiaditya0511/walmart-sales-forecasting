import nbformat

def extract_markdown_from_notebook(notebook_path, output_markdown_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, nbformat.NO_CONVERT)

    # Initialize a list to hold the Markdown content
    markdown_content = []

    # Iterate through the cells
    for cell in notebook.cells:
        # Check if the cell is a Markdown cell
        if cell.cell_type == 'markdown':
            markdown_content.append(cell.source)

    # Join the Markdown content with double newlines for separation
    full_markdown = '\n\n'.join(markdown_content)

    # Write the Markdown content to the output file
    with open(output_markdown_path, 'w', encoding='utf-8') as f:
        f.write(full_markdown)

# Example usage
notebook_path = 'Website/main/analysis.ipynb'  # Replace with your notebook path
output_markdown_path = 'Miscellaneous/analysis.md'  # Output file path
# extract_markdown_from_notebook(notebook_path, output_markdown_path)

# Example usage
notebook_path = 'Website/main/forecasting.ipynb'  # Replace with your notebook path
output_markdown_path = 'Miscellaneous/forecasting.md'  # Output file path
extract_markdown_from_notebook(notebook_path, output_markdown_path)