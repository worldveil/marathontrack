
def GetSecsFromTimestring(tstring):
	"""
	xx:xx:xx 
	format
	"""
	t_intervals = tstring.strip().split(":")
	return int(t_intervals[0]) * 3600 + int(t_intervals[1]) * 60 + int(t_intervals[2])