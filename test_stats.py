
from stats import mean

#write a test fcn
def test_mean():
        #checks to see if statement is true
        assert(mean([2,4]) ==3 )

test_mean()

def test_float_mean():
        assert(mean([1,2]) == 1.5)
test_float_mean()
