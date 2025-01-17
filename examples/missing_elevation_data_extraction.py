from sport_activities_features import ElevationIdentification
from sport_activities_features import TCXFile


tcx_file = TCXFile()
tcx_data = tcx_file.read_one_file('path_to_the_data')

elevations = ElevationIdentification(tcx_data['positions'])
"""Adds tcx_data['elevation'] = eg. [124, 21, 412] for each position"""
tcx_data.update({'elevations': elevations})
