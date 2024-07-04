import geopandas as gpd
from shapely.geometry import Polygon

# Create a GeoDataFrame
data = {
    'id': [1, 2, 3],
    'geometry': [Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                 Polygon([(1, 1), (2, 1), (2, 2), (1, 2)]),
                 Polygon([(2, 2), (3, 2), (3, 3), (2, 3)]),
]
}

gdf = gpd.GeoDataFrame(data, crs='EPSG:4326')

# Optionally, you can set the crs (Coordinate Reference System) of the GeoDataFrame
# gdf.crs = 'EPSG:4326'  # WGS84 coordinate system, if not already set

# Print GeoDataFrame to see the structure
# Define the output GeoPackage file path
output_gpkg = 'example.gpkg'

# Export GeoDataFrame to GeoPackage
gdf.to_file(output_gpkg, driver='GPKG')

print(f"GeoPackage file saved to: {output_gpkg}")
