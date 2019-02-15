import exputils
import os

def test_generate_experiments(tmpdir):

    dir_path = os.path.dirname(os.path.realpath(__file__))

    ################################################
    # test 1

    directory = os.path.join(tmpdir.strpath, 'test01')

    exputils.generate_experiment_files(os.path.join(dir_path, 'test_01.ods'), directory=directory, extra_files=[os.path.join(dir_path, 'extra_file_01'), os.path.join(dir_path, 'extra_file_02')])

    # group folders
    assert os.path.isdir(os.path.join(directory, 'group_01'))
    assert os.path.isdir(os.path.join(directory, 'group_02'))

    # experiment folder folders
    assert os.path.isdir(os.path.join(directory, 'group_01', 'experiment_000001'))
    assert os.path.isdir(os.path.join(directory, 'group_01', 'experiment_000003'))
    assert os.path.isdir(os.path.join(directory, 'group_02', 'experiment_000010'))
    assert os.path.isdir(os.path.join(directory, 'group_02', 'experiment_000030'))

    # experiment files
    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000001', 'file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000001', 'exp_1_file_02'))
    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000001', 'extra_file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000001', 'extra_file_02'))

    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000003', 'file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000003', 'exp_3_file_02'))
    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000003', 'extra_file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_01', 'experiment_000003', 'extra_file_02'))

    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000010', 'file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000010', 'exp_10_file_02'))
    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000010', 'extra_file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000010', 'extra_file_02'))

    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000030', 'file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000030', 'exp_30_file_02'))
    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000030', 'extra_file_01'))
    assert os.path.isfile(os.path.join(directory, 'group_02', 'experiment_000030', 'extra_file_02'))

    # file content
    with open(os.path.join(directory, 'group_01', 'experiment_000001', 'file_01'), 'r') as file:
        file_content = file.read()
    assert 'file 1:\n1\n1\nguten\n' == file_content

    with open(os.path.join(directory, 'group_01', 'experiment_000001', 'exp_1_file_02'), 'r') as file:
        file_content = file.read()
    assert 'file 2:\n3\nvielen\n' == file_content

    with open(os.path.join(directory, 'group_01', 'experiment_000003', 'file_01'), 'r') as file:
        file_content = file.read()
    assert 'file 1:\n3\n5\ntag\n' == file_content

    with open(os.path.join(directory, 'group_01', 'experiment_000003', 'exp_3_file_02'), 'r') as file:
        file_content = file.read()
    assert 'file 2:\n7\ndank\n' == file_content

    with open(os.path.join(directory, 'group_02', 'experiment_000010', 'file_01'), 'r') as file:
        file_content = file.read()
    assert 'file 1:\n10\n10\nguten\n' == file_content

    with open(os.path.join(directory, 'group_02', 'experiment_000010', 'exp_10_file_02'), 'r') as file:
        file_content = file.read()
    assert 'file 2:\n30\nvielen\n' == file_content

    with open(os.path.join(directory, 'group_02', 'experiment_000030', 'file_01'), 'r') as file:
        file_content = file.read()
    assert 'file 1:\n30\n50\ntag\n' == file_content

    with open(os.path.join(directory, 'group_02', 'experiment_000030', 'exp_30_file_02'), 'r') as file:
        file_content = file.read()
    assert 'file 2:\n70\ndank\n' == file_content

    ################################################
    # test 2

    directory = os.path.join(tmpdir.strpath, 'test02')

    exputils.generate_experiment_files(os.path.join(dir_path, 'test_02.ods'), directory=directory, extra_files=os.path.join(dir_path, 'extra_file_01'))

    # group folders
    assert os.path.isdir(os.path.join(directory))

    # experiment folder folders
    assert os.path.isdir(os.path.join(directory, 'experiment_000001'))
    assert os.path.isdir(os.path.join(directory, 'experiment_000003'))

    # experiment files
    assert os.path.isfile(os.path.join(directory, 'experiment_000001', 'file_01'))
    assert os.path.isfile(os.path.join(directory, 'experiment_000001', 'exp_1_file_02'))
    assert os.path.isfile(os.path.join(directory, 'experiment_000001', 'extra_file_01'))


    assert os.path.isfile(os.path.join(directory, 'experiment_000003', 'file_01'))
    assert os.path.isfile(os.path.join(directory, 'experiment_000003', 'exp_3_file_02'))
    assert os.path.isfile(os.path.join(directory, 'experiment_000003', 'extra_file_01'))

    # file content
    with open(os.path.join(directory, 'experiment_000001', 'file_01'), 'r') as file:
        file_content = file.read()
    assert 'file 1:\n1\n1\nguten\n' == file_content

    with open(os.path.join(directory, 'experiment_000001', 'exp_1_file_02'), 'r') as file:
        file_content = file.read()
    assert 'file 2:\n3\nvielen\n' == file_content

    with open(os.path.join(directory, 'experiment_000003', 'file_01'), 'r') as file:
        file_content = file.read()
    assert 'file 1:\n3\n5\ntag\n' == file_content

    with open(os.path.join(directory, 'experiment_000003', 'exp_3_file_02'), 'r') as file:
        file_content = file.read()
    assert 'file 2:\n7\ndank\n' == file_content
