#!/bin/bash

rrdtool graph temperature.png \
    -w 1000 -h 300 -a PNG \
    --slope-mode \
    --start -86400 --end now \
    --font DEFAULT:7: \
    --title "temperature" \
    --watermark "`date`" \
    --vertical-label "temperature (C)" \
    --lower-limit 0 \
    --x-grid MINUTE:10:HOUR:1:MINUTE:120:0:%R \
    --alt-y-grid --rigid \
    DEF:temperature=yocto_meto.rrd:temperature:MAX \
    LINE1:temperature#FF0000:"temperature (C)" \
    GPRINT:temperature:LAST:"Cur\: %5.2lf" \
    GPRINT:temperature:AVERAGE:"Avg\: %5.2lf" \
    GPRINT:temperature:MAX:"Max\: %5.2lf" \
    GPRINT:temperature:MIN:"Min\: %5.2lf\t\t\t" \
    COMMENT:"temperature"

rrdtool graph humidity.png \
    -w 1000 -h 300 -a PNG \
    --slope-mode \
    --start -86400 --end now \
    --font DEFAULT:7: \
    --title "humidity" \
    --watermark "`date`" \
    --vertical-label "humidity (%)" \
    --lower-limit 0 \
    --x-grid MINUTE:10:HOUR:1:MINUTE:120:0:%R \
    --alt-y-grid --rigid \
    DEF:humidity=yocto_meto.rrd:humidity:MAX \
    LINE1:humidity#0000FF:"humidity (%)" \
    GPRINT:humidity:LAST:"Cur\: %5.2lf" \
    GPRINT:humidity:AVERAGE:"Avg\: %5.2lf" \
    GPRINT:humidity:MAX:"Max\: %5.2lf" \
    GPRINT:humidity:MIN:"Min\: %5.2lf\t\t\t" \
    COMMENT:"humidity"

rrdtool graph pressure.png \
    -w 1000 -h 300 -a PNG \
    --slope-mode \
    --start -86400 --end now \
    --font DEFAULT:7: \
    --title "pressure" \
    --watermark "`date`" \
    --vertical-label "pressure (mbar)" \
    --lower-limit 1000 \
    --x-grid MINUTE:10:HOUR:1:MINUTE:120:0:%R \
    --alt-y-grid --rigid \
    DEF:pressure=yocto_meto.rrd:pressure:MAX \
    LINE1:pressure#008F00:"pressure (mbar)" \
    GPRINT:pressure:LAST:"Cur\: %5.2lf" \
    GPRINT:pressure:AVERAGE:"Avg\: %5.2lf" \
    GPRINT:pressure:MAX:"Max\: %5.2lf" \
    GPRINT:pressure:MIN:"Min\: %5.2lf\t\t\t" \
    COMMENT:"pressure"
