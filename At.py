import krpc
import math

def autoroll(activevessel , vesselref):
    bias = 0.005
    vesselFlight = activevessel.flight(vesselref)
    if vesselFlight.roll == 0:
        activevessel.control.sas=True
        return 0.
    elif vesselFlight.roll > 1:
        dg = (vesselFlight.roll/360)*2*math.pi
        return float((math.cos(dg)-1)*0.5-bias)
    elif vesselFlight.roll < -1:
        dg = (vesselFlight.roll/360)*2*math.pi 
        return float(-((math.cos(dg)-1)*0.5)+bias)


def autopitch(activevessel , vesselref):
    bias = 0.05
    vesselFlight = activevessel.flight(vesselref)
    if vesselFlight.pitch == 0:
        activevessel.control.sas=True
        activevessel.auto_pilot.targe_pitch=0
        activevessel.auto_pilot.engage()
        return 0.
    elif vesselFlight.pitch > 1:
        dg = (vesselFlight.pitch/360)*2*math.pi
        return float((math.cos(dg)-1))-bias
    elif vesselFlight.pitch < -1:
        dg = (vesselFlight.pitch/360)*2*math.pi 
        return float(-(math.cos(dg)-1))+bias
    
