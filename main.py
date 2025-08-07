import os
from scanner.walker import walk_directory
from scanner.interpreter import interpret_structure
from scanner.edwardizer import edwardize
from writer.markdown_writer import write_markdown

def main():
    target_dir = input("Which directory shall I explore?\n> ").strip()
    if not os.path.isdir(target_dir):
        print("That path is not a valid directory. Try again.")
        return

    raw_structure = walk_directory(target_dir)
    interpreted = interpret_structure(raw_structure)
    cosmic_structure = edwardize(interpreted)

    project_name = os.path.basename(os.path.abspath(target_dir))
    output_path = os.path.join("output", f"{project_name}_structure.md")
    write_markdown(cosmic_structure, output_path)

    print(f"\n* Structure report generated: {output_path}")

if __name__ == "__main__":
    main()
