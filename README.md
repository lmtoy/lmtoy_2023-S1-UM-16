# 2023-S1-UM-16

Source: G1.7+3.7-234
Project title: Molecular Clouds in the Fermi Bubble

This project maps some HVC's near the galactic center.

4 fields that need to be combined/mosaiced. 3 were observed, the NE field is missing.

See also 2024-S1-MX-2 for a followup, where also G358.7+3.7+179 was observed.

1. example manual running

SLpipeline.sh obsnum=110041 _s=G1.7+3.7-234 pix_list=-13 extent=600 restart=1 dv=10 dw=10
SLpipeline.sh obsnum=110041 _s=G1.7+3.7-234 oid=0 bank=0
SLpipeline.sh obsnum=110041 _s=G1.7+3.7-234 oid=1 bank=1 pix_list=-0,13

This is the local 12CO/13CO and shows the OFF position has some gas at V=-xxx

2.  Mark's manual version

SLpipeline.sh restart=1 obsnum=110041 dv=20 dw=80 pix_list=-12,13 oid=0 bank=0 vlsr=-234 rms_cut=4 x_extent=510 y_extent=510 b_order=2 otf_cal=1

This is focusing on the HVC velocity.
