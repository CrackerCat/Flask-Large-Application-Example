import unittest as ut

if __name__ == '__main__':
    all_tests = ut.TestLoader().discover('tests', pattern='*.py')
    ut.TextTestRunner().run(all_tests)
