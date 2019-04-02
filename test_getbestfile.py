import unittest

class Best_Student(unittest.TestCase):
	def test_Index(self):
		with self.assertRaises(IndexError, "index out of range"):
			print("index out of range")

if __name__=='__main__':
	unittest.main()
