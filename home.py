def extract ():
    return[10,20,30]

def transform(rows) :
    return [x * 2 for x in rows]

def main() :
    data = transform(extract())
    print(data)

if __name__ == "__main__":
    main()