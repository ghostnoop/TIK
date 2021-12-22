from algrotitms.MTF import MTF


class LZW(object):

    def findLongestPrefix(self, org, i, pCode, compressed, size):
        nextBy = 1
        p = org[i]
        includeLatestP = 0
        while nextBy < size - i:
            if p in pCode:
                nxt = org[i + nextBy]
                t = pCode.index(p)
                p = p + nxt
                nextBy += 1
                includeLatestP = 1
            else:
                includeLatestP = 0
                compressed += str(t)
                pCode.append(p)
                break
        if includeLatestP == 1:
            compressed += str(pCode.index(p))

        return pCode.index(p), len(p), compressed

    def encode(self, text: str):
        original_text = text
        alphabet = set(list(original_text))
        # original_text = input()
        size = len(original_text)
        pCode = list(alphabet)
        compressedText = ''
        p = ''
        start = 0
        length = 0

        while start < size:
            p, length, compressedText = self.findLongestPrefix(original_text, start, pCode, compressedText, size)
            if length > 2:
                start = start + len(pCode[p]) - 1
            else:
                start += 1

        print(pCode)
        print('compressed: ', compressedText)
        return compressedText

    def updatePcode(self, firstCharP, lastP, pCode):

        pc = lastP + firstCharP
        if pc not in pCode:
            pCode.append(pc)

        return pCode

    def decode(self, compressed_text: str, alphabet: list):
        original_text = ''
        size = len(compressed_text)
        pCode = list(alphabet)
        p = ''
        lastP = ''
        start = 0

        while start < size:
            lastP = p
            code = int(compressed_text[start])
            if code < len(pCode):
                p = pCode[code]
                if p in pCode:
                    original_text += str(p)
                    if lastP != '':
                        pCode = self.updatePcode(p[0], lastP, pCode)
                    start += 1
            else:
                pCode = self.updatePcode(lastP[0], lastP, pCode)
                p = pCode[code]
                original_text += str(p)
                pCode = self.updatePcode(p[0], lastP, pCode)
                start += 1
        print('decoded: ', original_text)
        return original_text


if __name__ == '__main__':
    ct = LZW().encode('abababbabaabbabbaabba')
    LZW().decode(ct, ['b', 'a'])
    dt = MTF().encode(str(ct))
    MTF().decode(dt)
