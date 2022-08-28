def upper(text):
    UC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    LC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                  "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    out = list()
    for i in range(len(text)):
        out.append(text[i])
        for j in range(len(LC)):
            if LC[j] == text[i]:
                out[i] = UC[j]
    return "".join(out)

def main():
    print(upper("Hello world"))

if __name__ == "__main__":
   main() 
