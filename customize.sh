# CHECK Installation Environment
if [ $BOOTMODE = false ]; then
	ui_print "- Installing through Custom Recovery Not Supported"
	ui_print "- Intsall this Module via Magisk Manager"
	abort "- ! Aborting installation !"
fi

package="com.google.android.youtube"

ui_print ""
ui_print "+ + + + + + + + + + + + + + + +"
ui_print "+      YouTube  ReVanced      +"
ui_print "+     ——————————————————      +"
ui_print "+          by AɾɑƒɑԵ          +"
ui_print "+     ——————————————————      +"
ui_print "+     Version : 17.37.35      +"
ui_print "+     ——————————————————      +"
ui_print "+  Patched Date : 22-09-2022  +"
ui_print "+ + + + + + + + + + + + + + + +"
ui_print ""
ui_print "+ + + + + + + + + + + + + + + + + + + +"
ui_print "+ Built With                          +"
ui_print "+ ——————————————————                  +"
ui_print "+ ✨ReVanced-cli-2.11.1-all.jar       +"
ui_print "+ ✨ReVanced-patches-2.65.0.jar       +"
ui_print "+ ✨ReVanced-integrations-0.41.1.apk  +"
ui_print "+ + + + + + + + + + + + + + + + + + + +"
ui_print "  ——————————————————————————————————"
ui_print ""
ui_print "- Theme : Light & Black "
ui_print ""
ui_print "  ——————————————————————————————————"

# Remove Vanced ReVanced Script
rm -rf /data/adb/vanced
rm -rf /data/adb/service.d/vanced.sh
rm -rf /data/adb/post-fs-data.d/vanced.sh
rm -rf /data/adb/revanced
rm -rf /data/adb/service.d/revanced.sh
rm -rf /data/adb/post-fs-data.d/revanced.sh

ui_print ""
ui_print "- Setting Permissions"
ui_print ""
chmod 644 $MODPATH/$package.apk
chown system:system $MODPATH/$package.apk
chcon u:object_r:apk_data_file:s0 $MODPATH/$package.apk
chmod +x $MODPATH/service.sh $MODPATH/post-fs-data.sh

if [[ "$( dumpsys package $package | grep versionName )" != *"17.38.32"* ]]; then 
ui_print "  ——————————————————————————————————"
ui_print ""
ui_print "- YouTube Not Found! Reinstalling..." && pm install -r -d $MODPATH/Stock.apk; fi
rm $MODPATH/Stock.apk
ui_print "  ——————————————————————————————————"
ui_print ""
ui_print "- Unmounting the apk"
ui_print ""
sh $MODPATH/post-fs-data.sh || true
ui_print "  ——————————————————————————————————"
ui_print ""
ui_print "- Mounting YouTube ReVanced..."
ui_print ""
sh $MODPATH/service.sh

# Uninstall Script
mv -f $MODPATH/YouTubeReVanced-uninstall.sh /data/adb/service.d/YouTubeReVanced-uninstall.sh
chmod +x /data/adb/service.d/YouTubeReVanced-uninstall.sh

# Disable battery optimization for YouTube ReVanced
ui_print "  ——————————————————————————————————"
ui_print ""
ui_print "- Disabling Battery Optimization"
ui_print ""
ui_print "  ——————————————————————————————————"
dumpsys deviceidle whitelist +$PK > /dev/null 2>&1
#temporary files removing
ui_print ""
ui_print "- Cleaning temp directory "
ui_print ""
rm -rf /data/local/tmp2
am start -a android.intent.action.VIEW -d "https://t.me/AndroidsRepo" &>/dev/null