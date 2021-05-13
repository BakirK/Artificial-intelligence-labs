import sys
sys.path.append('/Users/user/Downloads/pyke-1.1.1/examples/family_relations')
import driver
#
if len(sys.argv) == 3 :
	driver.fc_test2(str(sys.argv[1]), str(sys.argv[2]))
	print('sibling test 2')
	driver.sibling_test2(str(sys.argv[1]), str(sys.argv[2]))
else :
	driver.fc_test(str(sys.argv[1]))
	print('brother')
	driver.brother_test(str(sys.argv[1]))
	print('sister')
	driver.sister_test(str(sys.argv[1]))
	print('sibling')
	driver.sibling_test(str(sys.argv[1]))
	print('grand')
	driver.grandParent_test(str(sys.argv[1]))
	
# print(str(sys.argv[1]))
