def list_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
b64_file = open("./8.txt","r")
import base64
b64_decoded_text_decoded = ([base64.b64decode(x.strip()) for x in b64_file.readlines()])
b64_file.close()
multiples_of_sixteen = [((item + 1) * 16) for item in range(10)]
for elem in b64_decoded_text_decoded:
    for i in multiples_of_sixteen:
        current_list = list(list_chunks(elem,i))
        set_length = len(set(current_list))
        list_length = len(current_list)
        has_equals = (set_length != list_length)
        if has_equals == True:
            print("block size is: {}".format(i))
            print("text is:")
            print(base64.b64encode(elem))