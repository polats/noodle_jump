from smolagents import Tool

class FindFilesTool(Tool):
    name = "find_files"
    description = "Find files with a given extension in a directory and its subdirectories"
    inputs = {"extension":{"type":"string","description":"the place from which you start your ride"}}
  
    output_type = "string"

    def forward(self, extension: str) -> str:
        """
        Recursively search for files with a given extension in a directory and its subdirectories.

        Args:
            extension: The file extension to look for (e.g., '.txt')
        """
        import os

        root_dir = "./"
        found_files = []

        # Walk through the directory tree
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(extension):
                    filepath = os.path.join(dirpath, filename)
                    found_files.append(filepath)

        return found_files