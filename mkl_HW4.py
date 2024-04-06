from console_gfx import ConsoleGfx


def to_hex_string(data):
    hexString = ""

    for i in data:
        match i:
            case 10:
                hexString += 'a'
            case 11:
                hexString += 'b'
            case 12:
                hexString += 'c'
            case 13:
                hexString += 'd'
            case 14:
                hexString += 'e'
            case 15:
                hexString += 'f'
            case _:
                hexString += str(i)

    return hexString


def count_runs(flat_data):
    count = 0
    runs = 1

    for i in range(len(flat_data) - 1):
        if flat_data[i] != flat_data[i + 1]:
            runs += 1
            count = 0
        else:
            count += 1

        if count == 15:
            runs += 1
            count = 0

    return runs


def encode_rle(flat_data):
    rleList = []
    count = 1

    for i in range(len(flat_data) - 1):
        if flat_data[i] == flat_data[i + 1]:
            count += 1

            if count == 15:
                rleList.append(15)
                rleList.append(flat_data[i])
                count = 0
        else:
            rleList.append(count)
            rleList.append(flat_data[i])
            count = 1

    if count != 0:
        rleList.append(count)
        rleList.append(flat_data[-1])

    return rleList


def get_decoded_length(rle_data):
    length = 0

    for i in rle_data[::2]:
        length += i

    return length


def decode_rle(rle_data):
    decodedList = []

    for i in range(0, len(rle_data), 2):
        decodedList.extend([rle_data[i + 1]] * rle_data[i])

    return decodedList


def string_to_data(data_string):
    rleList = []

    for i in data_string:
        match i:
            case 'a':
                rleList.append(10)
            case 'b':
                rleList.append(11)
            case 'c':
                rleList.append(12)
            case 'd':
                rleList.append(13)
            case 'e':
                rleList.append(14)
            case 'f':
                rleList.append(15)
            case _:
                rleList.append(int(i))

    return rleList


def to_rle_string(rle_data):
    hexString = ""

    for i in range(0, len(rle_data), 2):
        hexString += str(rle_data[i])

        if rle_data[i + 1] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            hexString += f"{str(rle_data[i + 1])}:"
        else:
            match (rle_data[i + 1]):
                case 10:
                    hexString += 'a:'
                case 11:
                    hexString += 'b:'
                case 12:
                    hexString += 'c:'
                case 13:
                    hexString += 'd:'
                case 14:
                    hexString += 'e:'
                case 15:
                    hexString += 'f:'

    return hexString.rstrip(':')


def string_to_rle(rle_string):
    splitString = rle_string.split(':')
    rleList = []

    for i in splitString:
        rleList.append(int(i[:-1]))

        if i[-1] in "0123456789":
            rleList.append(int(i[-1]))
        else:
            match (i[-1]):
                case 'a':
                    rleList.append(10)
                case 'b':
                    rleList.append(11)
                case 'c':
                    rleList.append(12)
                case 'd':
                    rleList.append(13)
                case 'e':
                    rleList.append(14)
                case 'f':
                    rleList.append(15)

    return rleList

def main():

    check = True
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    dataString = -1

    while(check):
        print("RLE Menu\n--------")
        print("0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data")
        choice = int(input("Select a Menu Option: "))

        if(choice == 0):
            check = False
        elif(choice == 1):
            fileName = input("Enter name of file to load: ")
            dataString = ConsoleGfx.load_file(fileName)
        elif(choice == 2):
            dataString = ConsoleGfx.test_image
            print("Test image data loaded.")
        elif(choice==3):
            String = input("Enter an RLE string to be decoded: ")
            dataString = decode_rle(string_to_rle(String))
        elif(choice==4):
            String = input("Enter the hex string holding RLE data: ")
            dataString = decode_rle(string_to_data(String))
        elif(choice==5):
            String = input("Enter the hex string holding flat data: ")
            dataString = string_to_data(String)
        elif(choice==6):
            print("Displaying image...")
            if dataString == -1:
                print("(no data)")
            else:
                ConsoleGfx.display_image(dataString)
        elif(choice==7):
            print("RLE representation: ")
            if dataString == -1:
                print("(no data)")
            else:
                print(to_rle_string(encode_rle(dataString)))
        elif(choice==8):
            print("RLE hex values: ")
            if dataString == -1:
                print("(no data)")
            else:
                print(to_hex_string(encode_rle(dataString)))
        elif(choice==9):
            print("Flat hex values: ")
            if dataString == -1:
                print("(no data)")
            else:
                print(to_hex_string(dataString))
        else:
            print("Error! Invalid input.")

if __name__ == "__main__":
    main()