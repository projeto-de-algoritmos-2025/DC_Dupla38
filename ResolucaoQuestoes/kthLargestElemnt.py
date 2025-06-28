class Solution:
    def findKthLargest(self, nums, k):
        def select(arr, k):
            if len(arr) <= 10:
                return sorted(arr, reverse=True)[k - 1]

            grupos = [arr[i:i+5] for i in range(0, len(arr), 5)]
            medianas = [sorted(grupo)[len(grupo) // 2] for grupo in grupos]
            pivot = select(medianas, len(medianas) // 2 + 1)

            maiores = [x for x in arr if x > pivot]
            iguais = [x for x in arr if x == pivot]
            menores = [x for x in arr if x < pivot]

            if k <= len(maiores):
                return select(maiores, k)
            elif k <= len(maiores) + len(iguais):
                return pivot
            else:
                return select(menores, k - len(maiores) - len(iguais))

        return select(nums, k)
