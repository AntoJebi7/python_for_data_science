import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a Basemap instance
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='l')

# Draw map features
m.drawcoastlines()
m.drawcountries()
m.drawstates()

# Plot data points (city locations)
cities = {
    'Los Angeles': (-118.40, 34.05),
    'New York': (-73.94, 40.71),
    'Paris': (2.35, 48.85),
    'Tokyo': (139.69, 35.68)
}
lons, lats = zip(*cities.values())
x, y = m(lons, lats)
m.plot(x, y, 'bo', markersize=8)

# Show the map
plt.title('Cities on World Map')
plt.show()

