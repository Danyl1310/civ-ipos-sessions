def main():
    # TODO Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal
    #text to bytes

    def text_to_bytes(text):
        bytes_data = text.encode("utf-8")
        return bytes_data
    #byte to text
    def byte_to_text(data):
        unicode_data = data.decode("utf-8")
        return unicode_data
    #text to bytes
    def byte_reversal(bytes_data):
        bytes_data = bytes_data[::-1]
        return bytes_data

    # Main program logic
    # TODO Open the binary file for reading and create output text and bytes files for writing using the context manager
    with open("data.bin", "rb") as file:
        try:

                    # Iterate through each line in the binary file
                    for line in file:
                        # TODO Decode the line to Unicode string and remove leading/trailing whitespaces
                        line = byte_to_text(line)
                        # Check if the line starts with "TEXT:"
                        if line.startswith("TEXT:"):
                            # Extract text content, convert to uppercase, and write to text file
                            text_to_print = line[5:].upper()
                            with open("converted_text.txt", "w") as text_output:
                                text_output.write(text_to_print + '\n')

                        # Check if the line starts with "BYTES:"
                        elif line.startswith("BYTES:"):
                            # TODO Extract the string and encode to hexadecimal
                            hexa_data = line.encode("hex")
                            print("Convert-Hex:", hexa_data)
                            pass
                            # TODO Extract byte content, convert to bytes object(using fromhex()),
                            bytes_data = bytes.fromhex(line)
                            print(bytes_data)
                            # Using your helper functions
                            # TODO 1. reverse bytes, and write to bytes file
                            bytes_data = bytes_data[::-1]
                            print(bytes_data)
                            bytes_data = bytes_data[2:]
                            with open("bytes.bin", "wb") as file:
                                file.write(bytes_data)
                            # TODO 2. convert back to text
                            bytes_data = bytes_data.decode("hex")
                            print(bytes_data)
                            # TODO 3. convert back to bytes
                            bytes_data = bytes_data.encode("utf-8")
                            print(bytes_data)

                            # Write the bytes data
                            with open("converted_text.txt", "w") as bytes_output:
                                bytes_output.write(bytes_data)
    # TODO use the in built IOError class                 
        except:
            pass
        # Handle file I/O errors
        # IOError - see definition, also Documentation: https://docs.python.org/3/library/io.html#
        # print(binary_error_message.strerror)

        # Handle other exceptions using the exception class
        
if __name__ == "__main__":
    main()