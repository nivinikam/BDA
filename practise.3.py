from mrjob.job import MRJob
from mrjob.step import MRStep
import string

class wordfreq(MRJob):
    uin = [word.strip().lower() for word in input("Enter input: ").lower().split(',')]

    def steps(self):
        return [MRStep(mapper=self.mapper_extract,reducer=self.reducer)]
    
    def mapper_extract(self,_,text):
        translator = str.maketrans('','',string.punctuation)
        text_without_punctuation = text.translate(translator)

        word_list = text_without_punctuation.split()

        for word in word_list:
            yield word.lower(),1

    def reducer(self,key,values):
        if key in self.uin:
            yield key,sum(values)

if __name__ =="__main__":
    wordfreq.run()                    