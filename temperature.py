# -*- coding: utf-8 -*-
import datetime
import os.path

from subprocess import call

from yoctopuce.yocto_api import *
from yoctopuce.yocto_temperature import *
from yoctopuce.yocto_humidity import *
from yoctopuce.yocto_pressure import *


log = "/Users/tom/Desktop/temp-{:%Y%m%d}.log".format(timestamp)
rrd = "yocto_meto.rrd"

errmsg = YRefParam()
YAPI.RegisterHub("usb", errmsg)

timestamp = datetime.datetime.now()
temperature = YTemperature.FirstTemperature()
humidity = YHumidity.FirstHumidity()
pressure = YPressure.FirstPressure()

# print "{}°C".format(temperature.get_currentValue())
# print "{} %RH".format(humidity.get_currentValue())
# print "{} mbar".format(pressure.get_currentValue())


def get_currentValue(sensor):
    try:
        return sensor.get_currentValue()
    except:
        return ''


if not os.path.isfile(rrd):
    step = 60

    temperature = "DS:temperature:GAUGE:120:0:50"
    humidity = "DS:humidity:GAUGE:120:0:100"
    pressure = "DS:pressure:GAUGE:120:200:1100"

    day = "RRA:MAX:0.5:1:1440"

    cmd = "rrdtool create {} --step {} {} {} {} {}"

    subprocess.call(
        cmd.format(rrd, step, temperature, humidity, pressure, day),
        shell=True
    )

data = "{:%s}:{}:{}:{}\n".format(
    timestamp,
    get_currentValue(temperature),
    get_currentValue(humidity),
    get_currentValue(pressure)
)

cmd = "rrdtool update {} --template temperature:humidity:pressure {}"
subprocess.call(
    cmd.format(rrd, data),
    shell=True
)

with open(log, 'a') as log:
    log.write(data.replace(':', ','))
