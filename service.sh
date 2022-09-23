#!/system/bin/sh
while [ "$(getprop sys.boot_completed | tr -d '\r')" != "1" ]; do sleep 1; done

MODDIR=${0%/*}
package="com.google.android.youtube"
base_path="$MODDIR/$package.apk"
stock_path=$( pm path $package | grep base | sed 's/package://g' )

chcon u:object_r:apk_data_file:s0 $base_path

mount -o bind $base_path $stock_path