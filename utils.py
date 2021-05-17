import base64


def read_binary_file(filename):
    with open(filename, 'rb') as binary_file:
        binary_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_data)
        return base64_encoded_data.decode('utf-8')


def string_to_content(string_content):
    return base64.b64encode(string_content.encode('ascii')).decode('ascii')
