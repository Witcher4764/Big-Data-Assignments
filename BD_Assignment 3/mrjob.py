from mrjob.job import MRJob
from mrjob.step import MRStep

class wordcount(MRJob):
    
    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield word, 1
    
    def reducer(self, key, values):
        yield key, sum(values)

    
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
            
        ]

if __name__ == '__main__':
    wordcount.run()
