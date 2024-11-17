def test_running_time(operation, run_time):
    """ write run time to file """
    with open('run_time.txt', 'a') as file:
        file.write(('{0}: {1}\n').format(operation, run_time))