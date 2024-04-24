from mrjob.job import MRJob
from mrjob.step import MRStep
import string

class Wordfre(MRJob):
    uin = [word.strip().lower()for word in input("enter the word: ").lower().split()]

    def step(self):
        return [MRStep(mapper=self.mapper_extract_words,reducer=self.reducer)]
    

    def mapper_extract_words(self,_,text):
        translator = str.maketrans('','',string.punctuation)
        text_without_punctuation = text.translate(translator)
        word_list=text_without_punctuation.split()

        for word in word_list:
            yield word.lower,1

    def reducer(self,key,values):
        if key in self.uin:
            yield key,sum(values)  

if __name__ == "__main__":
    Wordfre.run()
                  