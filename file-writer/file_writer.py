def write_to_file(filename, content):
    with open(filename,'w') as f:
        f.write(content)

if __name__== "__main__":
    write_to_file('output.txt', 'hello from python script!')
    print("file created and content written.")