class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        sorted_array = sorted(folder)
        result = [sorted_array[0]]

        for i in range(1, len(folder)):
            current_folder = sorted_array[i]
            last_added = result[-1]

            if not current_folder.startswith(last_added + '/'):
                result.append(current_folder)
        
        return result