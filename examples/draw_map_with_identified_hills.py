"""
This example presents how to draw a map with identified hills.
"""
from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.plot_data import PlotData
from sport_activities_features.tcx_manipulation import TCXFile


# read TCX file
tcx_file = TCXFile()
(
    activity_type,
    positions,
    altitudes,
    distances,
    total_distance,
    timestamps,
    heartrates,
    speeds
) = tcx_file.read_one_file('path_to_the_data').values()

# detect hills in data
Hill = HillIdentification(altitudes, 30)
Hill.identify_hills()
all_hills = Hill.return_hills()

# draw detected hills
Map = PlotData()

Map.draw_hills_in_map(altitudes, distances, all_hills)
