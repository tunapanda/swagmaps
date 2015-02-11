Swagmap for KTouch
==================

This swagmap is intended to be used together with [KTouch](https://edu.kde.org/applications/all/ktouch) 
and [ktouchxapi](https://github.com/tunapanda/ktouchxapi).
KTouch saves statistics files that ktouchxapi reads. Ktouchxapi then saves records for the progress of each
user in an xAPI record store, and this swagmap shows which of the levels the user has completed.

For this to work together some configuration needs to be done. The swagmap is created to show progress for xAPI
objectives that look like this:

    http://ktouch.tunapanda.org/tunapanda.ktouch.xml#5

Where the `5` is the level, running from `0` to `15` inclusive for the 16 levels.

The `tunapanda.ktouch.xml` part is the filename of the KTouch lecture that the user has practiced.

The `http://ktouch.tunapanda.org/` part is a somewhat arbitrary string that ktouchxapi needs to be configured
to save using the `--targetPrefix` option of that program.
