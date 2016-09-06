def pytest_report_header(startdir):
    return 'hello: ' + str(startdir)

