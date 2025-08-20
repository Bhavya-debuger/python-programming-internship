import os

def rename_files_in_folder(folder_path, pattern="file_{}.txt"):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for idx, filename in enumerate(files, 1):
        ext = os.path.splitext(filename)[1]
        new_name = pattern.format(idx)
        # Ensure extension is .txt
        if not new_name.endswith('.txt'):
            new_name += '.txt'
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed '{filename}' to '{new_name}'")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    rename_files_in_folder(folder)