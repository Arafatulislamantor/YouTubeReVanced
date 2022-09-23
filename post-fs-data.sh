#!/system/bin/sh

package="com.google.android.youtube"
stock_path=$( pm path $package | grep base | sed 's/package://g' )
umount -l $stock_path