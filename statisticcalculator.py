import numpy as np
import os
import glob

def calc_experiment_statistics(statistics, load_experiment_data_func,  *args, statistics_directory='statistics', recalculate_statistics=False, verbose=False):
    '''

    :param statistics: List with tuples of the form: (statistic name, statistic function)
    :param args: Directoryies in which the experiments are for which the statistics should be computed.
    :param results_directory:
    :param statistics_directory:
    :return:
    '''

    if len(args) == 0:
        experiments = ['.']
    elif len(args) == 1 and isinstance(args[0], list):
        experiments = args[0]
    else:
        experiments = list(args)

    def get_data(data, experiment_folder):
        '''Loads the data if the data is not already loaded'''
        if data is None:
            data = load_experiment_data_func(experiment_folder)
        return data


    # identify the experiment folders
    experiment_folders = []
    for folder in experiments:

        found_folders = []

        # make sure the folder has folder form, i.e. with final '/'
        # then take the base directory and search in it
        # this makes sure, that also the direct given folder is looked after, e.g. './experiment_000001' would also be identified
        basedir = os.path.dirname(os.path.join(folder, ''))
        directory_name = os.path.basename(os.path.dirname(basedir))

        # look if directory itself is a repetition experiment
        if directory_name.find('repetition_') and os.path.isdir(basedir):
            found_folders.append(basedir)

        # look if there are repetition folders somewhere inside the directory
        if not found_folders:
            for foldername in glob.iglob(os.path.join(basedir,'**','repetition_*'), recursive=True):
                if os.path.isdir(foldername):
                    found_folders.append(foldername)

        # if there are no repetitions, then search for experiment folder
        if not found_folders:
            if directory_name.find('experiment_') and os.path.isdir(basedir):
                found_folders.append(basedir)

        if not found_folders:
            for foldername in glob.iglob(os.path.join(basedir, '**', 'experiment_*'), recursive=True):
                if os.path.isdir(foldername):
                    found_folders.append(foldername)

        if not found_folders:
            # assume the given folder is the the one
            found_folders.append(folder)

        experiment_folders.extend(found_folders)

    # calc statistic if it does not exist already
    for experiment_folder in sorted(experiment_folders):

        data = None

        directory = os.path.join(experiment_folder, statistics_directory)

        if not os.path.isdir(directory):
            os.makedirs(directory)

        if verbose:
            print('Calculate statistics for {!r}:'.format(experiment_folder))

        for statistic_name, statistic_func in statistics:

            # calculate statistics if they do not exist
            filename = '{}.npy'.format(statistic_name)

            filepath = os.path.join(directory, filename)
            if not os.path.isfile(filepath) or recalculate_statistics:

                if verbose:
                    print('\t{} ...'.format(statistic_name))

                data = get_data(data, experiment_folder)

                stat = statistic_func(data)

                np.save(filepath, stat)