class Solution:
    def reversePairs(self, nums):
        def sort_and_count(lst):
            n = len(lst)
            if n <= 1:
                return 0, lst

            meio = n // 2
            inv_esq, esq = sort_and_count(lst[:meio])
            inv_dir, dir = sort_and_count(lst[meio:])
            inv_merge, merged = merge_and_count(esq, dir)

            return inv_esq + inv_dir + inv_merge, merged

        def merge_and_count(esq, dir):
            count = 0
            j = 0
            for i in range(len(esq)):
                while j < len(dir) and esq[i] > 2 * dir[j]:
                    j += 1
                count += j

            merged = []
            i = j = 0
            while i < len(esq) and j < len(dir):
                if esq[i] <= dir[j]:
                    merged.append(esq[i])
                    i += 1
                else:
                    merged.append(dir[j])
                    j += 1
            merged.extend(esq[i:])
            merged.extend(dir[j:])
            return count, merged

        count, _ = sort_and_count(nums)
        return count
