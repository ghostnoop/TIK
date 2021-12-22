from collections import Counter
import numpy as np


class AlgoritmCoding(object):
    def encode(self, text: str):
        res = Counter(text)
        m = len(res)
        N = 5
        a = np.zeros((m, 5), dtype=object)

        keys = list(res.keys())
        value = list(res.values())
        total = sum(value)

        a[m - 1][3] = 0
        for i in range(m):
            a[i][0] = keys[i]
            a[i][1] = value[i]
            a[i][2] = ((value[i] * 1.0) / total)
        i = 0
        a[m - 1][4] = a[m - 1][2]
        while i < m - 1:
            a[m - i - 2][4] = a[m - i - 1][4] + a[m - i - 2][2]
            a[m - i - 2][3] = a[m - i - 1][4]
            i += 1

        strlist = list(text)
        Lenco = []
        Uenco = []
        Lenco.append(0)
        Uenco.append(1)

        for i in range(len(strlist)):
            result = np.where(a == keys[keys.index(strlist[i])])
            llistadd = (Lenco[i] + (Uenco[i] - Lenco[i]) * float(a[result[0], 3]))
            ulistadd = (Lenco[i] + (Uenco[i] - Lenco[i]) * float(a[result[0], 4]))

            Lenco.append(llistadd)
            Uenco.append(ulistadd)

            tag = (Lenco[-1] + Uenco[-1]) / 2.0

        Lenco.insert(0, " Lower Range")
        Uenco.insert(0, "Upper Range")
        print(tag)

    def decode(self, text, m, a, tag):
        ltag = 0
        utag = 1
        decoded_string = []
        for i in range(len(text)):
            decodenum = ((tag - ltag) * 1.0) / (utag - ltag)
            for i in range(m):
                if (float(a[i, 3]) < decodenum < float(a[i, 4])):
                    decoded_string.append(str(a[i, 0]))
                    ltag = float(a[i, 3])
                    utag = float(a[i, 4])
                    tag = decodenum


if __name__ == '__main__':
    ac = AlgoritmCoding()
    ac.encode('ewrwwr')

