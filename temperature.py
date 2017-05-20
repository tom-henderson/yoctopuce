# -*- coding: utf-8 -*-
import datetime
from yoctopuce.yocto_api import *
from yoctopuce.yocto_temperature import *
from yoctopuce.yocto_humidity import *
from yoctopuce.yocto_pressure import *

errmsg = YRefParam()
YAPI.RegisterHub("usb", errmsg)

temperature = YTemperature.FirstTemperature()
humidity = YHumidity.FirstHumidity()
pressure = YPressure.FirstPressure()

# print "{}°C".format(temperature.get_currentValue())
# print "{} %RH".format(humidity.get_currentValue())
# print "{} mbar".format(pressure.get_currentValue())

timestamp = datetime.datetime.now()
log = "/Users/tom/Desktop/temp-{:%Y%m%d}.log".format(timestamp)


def get_currentValue(sensor):
    try:
        return sensor.get_currentValue()
    except:
        return ''


with open(log, 'a') as log:
    log.write(
        "{}, {}, {}, {}\n".format(
            timestamp.isoformat(),
            get_currentValue(temperature),
            get_currentValue(humidity),
            get_currentValue(pressure)
        )
    )
