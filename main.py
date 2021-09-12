#!/usr/bin/python3
from djitellopy import TelloSwarm

def call_swarm():
	print("assembling swarm")
	#absolute path m9
	dronelist='/opt/dronenetlist'
	fo=open(dronelist, "r")
	if(fo.read(10)==None):
		print("drone list not found or null")
		fo.close()
		exit()
	else:
		fo.close()
		assembly = TelloSwarm.fromFile(dronelist)
		return assembly

def connect_and_run(swarm):
	swarm.connect()
	print("performing health check routine")
	for drone in swarm:
		print("IP: " + str(drone) + " Battery: " + str(drone.get_battery()))
	swarm.end()



if __name__ == "__main__":
	connect_and_run(call_swarm())