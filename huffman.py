import os
import heapq

class HuffmanCoding:
    def __init__(self,path):
        self.path = path
        self.heap = []
        self.codes = {}

    class HeapNode:
        def __init__(self,char,freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        # comparator functions
        def __lt__(self,other):
            return self.freq < other.freq

        def __eq__(self,other):
            if(other == None):
                return False
            if(not isinstance(other,HuffmanCoding.HeapNode)):
                return False
            return self.freq == other.freq
        
    
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
        for key in frequency:
            node = HeapNode(key,frequency[key])
            heapq.heappush(self.heap,node)
        
    def merge_codes(self):
        #build huffman tree. Save root node in heap
        while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None,node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap,merged)

    def make_codes_helper(self,node,current_code):
        #make codes for each character
        if node == None:
            return

        if node.char != None:
            self.codes[node.char] = current_code
            return

        self.make_codes_helper(node.left,current_code + "0")
        self.make_codes_helper(node.right,current_code + "1")

    def make_codes(self):
        #make codes for each character ans save 0010110
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root,current_code)
        

    def get_encoded_text(self,text):
        #return encoded text
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]

        return encoded_text
        

    def pad_encoded_text(self,encoded_text):
        #pad encoded text
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"
        
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text

    def get_byte_array(self,padded_encoded_text):
        #return byte array 8 bits to byte
        b = bytearray()
        for i in range(0,len(padded_encoded_text),8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte,2))
        return b

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

