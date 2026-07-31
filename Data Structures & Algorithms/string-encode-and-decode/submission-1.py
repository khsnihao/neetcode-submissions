class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s    # 5#hello5#world
        return encoded_string 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # 1. Read full number
            while s[j] != "#":
                # 2. Move past '#'
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            # 3. Extract string
            res.append(s[i:j])
            # 4. Move pointer
            i = j
        return res
            

