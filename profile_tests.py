import nose
import cProfile
command = """nose.main(argv=['--ckan','--with-pylons=test-core.ini', 'ckan/tests', '-x', '-v'])"""
cProfile.runctx( command, globals(), locals(), filename="ckan.profile" )