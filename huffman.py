import os

class HuffmanCoding:
    def __init__(self,path):
        self.path = path
        self.heap = []
        self.codes = {}

    def make_frequency_dict(text):
        '''Calculate frequency and return dict '''
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self,frequency):
        # make priority queue
        pass

    def merge_codes(self):
        #build huffman tree. Save root node in heap
        pass

    def make_codes(self):
        #make codes for each character ans save
        pass

    def get_encoded_text(self,text):
        #return encoded text
        pass

    def pad_encoded_text(self,encoded_text):
        #pad encoded text
        pass

    def get_byte_array(self,padded_encoded_text):
        #return byte array 8 bits to byte
        pass

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file,open(output_path,'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)

            self.make_heap(frequency)
            self.merge_codes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
        
        print("Your file is Compressed")
        return output_path

