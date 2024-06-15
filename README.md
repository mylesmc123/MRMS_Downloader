# MRMS Downloader
The MRMS Downloader.py file will download a given startdate and enddate of MRMS data from the [Iowa State Mesonet MRMS repository](https://mtarchive.geol.iastate.edu/) website.

GRIB2 data is downloaded, and to be used in HEC-RAS or HEC-HMS needs to be run through HEC-Vortex to convert to DSS.

The output DSS data used for GLO to look specifcally at Hurricane Harvey 2017 is located at: "V:\projects\p00659_dec_glo_phase3\01_processing\MRMS\Harvey_Precip_MRMS.dss"

This script is based on Mark Bartlett's Databricks Jupyter notebook accessible to Water Institute Employees [MRMS_Downloader](https://dbc-9d1717f8-d468.cloud.databricks.com/?o=5992598613794601#notebook/558482802214000). This notebook is also available in this repo as: "MRMS_data_Comparison 1.ipynb"


## Note
Some MRMS Data is available as "MultiSensor_QPE_01H_Pass2" and some data is available as "GaugeCorr_QPE_01H". The base URL may need to be adjusted for your timewindow.