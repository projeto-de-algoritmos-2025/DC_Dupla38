from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Função recursiva que resolve o skyline para buildings[i:j]
        def dc(i, j):
            if i == j:
                L, R, H = buildings[i]
                return [[L, H], [R, 0]]
            mid = (i + j) // 2
            left_sky = dc(i, mid)
            right_sky = dc(mid+1, j)
            return merge(left_sky, right_sky)
        
        # Merge de dois skylines
        def merge(left, right):
            h1 = h2 = 0
            i = j = 0
            out = []
            cur_y = 0
            
            # varre os pontos dos dois skylines
            while i < len(left) and j < len(right):
                x1, y1 = left[i]
                x2, y2 = right[j]
                
                if x1 < x2:
                    x, h1 = x1, y1
                    i += 1
                elif x2 < x1:
                    x, h2 = x2, y2
                    j += 1
                else:  # mesmo eixo x
                    x = x1
                    h1 = y1
                    h2 = y2
                    i += 1
                    j += 1
                
                max_h = max(h1, h2)
                if cur_y != max_h:
                    out.append([x, max_h])
                    cur_y = max_h
            
            out.extend(left[i:])
            out.extend(right[j:])
            return out
        
        if not buildings:
            return []
        return dc(0, len(buildings) - 1)