
from stats import mean
from nose.tools import assert_equal, assert_almost_equal


#write a test fcn
def test_mean():
        #checks to see if statement is true
        #assert(mean([2,4])==3)
        assert_equal(mean([2.0,4.0]),3)
#test_mean()

def test_float_mean():
        #assert(mean([1,2]) == 1.5)
        assert_equal(mean([1.0,2.0]), 1.5)
#test_float_mean()

def test_neg_mean():
	#assert(mean([-2,2,4]) == 1.333)
	assert_almost_equal(mean([-2.0,2.0,4.0]), 1.333, places=3)
#test_neg_mean()
