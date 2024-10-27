import collections

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        result = []
        folder_path = folder[0].split('/')
        for path in folder[1:]:
            path = path.split('/')
            if folder_path != path[:len(folder_path)]:
                result.append('/'.join(folder_path))
                folder_path = path
            else:
                continue
        return result + ['/'.join(folder_path)]