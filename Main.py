from Pages.TestCase import PenIoTestCase

testCase = PenIoTestCase()
testCase.setUp()
testCase.testCreatePage('kopysovdass', 'Qwerty1q')
testCase.testEditingPage()
testCase.testUpdatePage('kopysovda', 'Qwerty1')
testCase.tearDown()