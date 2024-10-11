import os

def extract_text_from_files(root_folder, output_file):
    with open(output_file, 'w') as outfile:
        # Traverse the directory structure
        for foldername, subfolders, filenames in os.walk(root_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                
                try:
                    # Read text content from the file
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        # Write the filename as a separator in the output file
                        outfile.write(f"\n===== {file_path} =====\n\n")
                        # Write the content of the file
                        outfile.write(infile.read())
                        outfile.write("\n\n")
                except Exception as e:
                    # Handle any exceptions (like unsupported file types)
                    print(f"Could not read {file_path}: {e}")

if __name__ == "__main__":
    # Define the root folder and output file
    root_folder = "path_to_your_folder"  # Replace with your folder path
    output_file = "output.txt"
    
    extract_text_from_files(root_folder, output_file)
