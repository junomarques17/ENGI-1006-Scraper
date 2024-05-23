def text_to_list(text):
    li = [line for line in text.split('\n') if line]
    return li

def extract_names(li, key_str):
    key_section = False
    names = []
    for item in li:
        if key_str in item:
            key_section = True
            continue
        if key_section:
            if '@' in item:  # Check if the line contains an email
                # Split the line by spaces and ignore the last part (email)
                name = ' '.join(item.split()[:-1])
                names.append(name)
            else:
                break  # If the line does not contain an email, exit the section

    return names