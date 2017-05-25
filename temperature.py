# -*- coding: utf-8 -*-
import datetime
import os.path

import subprocess

from yoctopuce.yocto_api import *
from yoctopuce.yocto_temperature import *
from yoctopuce.yocto_humidity import *
from yoctopuce.yocto_pressure import *

rrdtool = "/usr/local/bin/rrdtool"

errmsg = YRefParam()
YAPI.RegisterHub("usb", errmsg)

timestamp = datetime.datetime.now()
temperature = YTemperature.FirstTemperature()
humidity = YHumidity.FirstHumidity()
pressure = YPressure.FirstPressure()

# print "{}°C".format(temperature.get_currentValue())
# print "{} %RH".format(humidity.get_currentValue())
# print "{} mbar".format(pressure.get_currentValue())

path = os.path.dirname(os.path.realpath(__file__))

log = "{}/temp-{:%Y%m%d}.csv".format(path, timestamp)
rrd = "{}/yocto_meto.rrd".format(path)


def get_currentValue(sensor):
    try:
        return sensor.get_currentValue()
    except:
        return ''


if not os.path.isfile(rrd):
    step = 60

    ds_temperature = "DS:temperature:GAUGE:120:0:50"
    ds_humidity = "DS:humidity:GAUGE:120:0:100"
    ds_pressure = "DS:pressure:GAUGE:120:200:1100"

    rra_day = "RRA:MAX:0.5:1:10080"

    cmd = "{} create {} --step {} {} {} {} {}"

    subprocess.call(
        cmd.format(
            rrdtool, rrd, step,
            ds_temperature, ds_humidity, ds_pressure,
            rra_day
        ),
        shell=True
    )

data = "{:%s}:{}:{}:{}".format(
    timestamp,
    get_currentValue(temperature),
    get_currentValue(humidity),
    get_currentValue(pressure)
)

cmd = "{} update {} --template temperature:humidity:pressure {}"
subprocess.call(
    cmd.format(rrdtool, rrd, data),
    shell=True
)

with open(log, 'a') as log:
    log.write(
        "{}\n".format(data.replace(':', ','))
    )
