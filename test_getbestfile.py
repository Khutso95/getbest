import unittest

class Best_Student(unittest.TestCase):
	"""Test class"""
	def test_index_out_of_range(self):
		with self.assertRaises(IndexError, "index out of range"):
			print("index out of range")

if __name__=='__main__':
	unittest.main()
