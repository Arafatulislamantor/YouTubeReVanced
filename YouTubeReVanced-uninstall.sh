#!/system/bin/sh

# Wait till device boot process complets
while [ "$(getprop sys.boot_completed)" != "1" ]; do
	sleep 1
done

sleep 10

# If YouTube ReVanced module is uninstalled then uninstall YouTube app on next boot
if [[ ! -d /data/adb/modules/YouTubeReVanced || -f /data/adb/modules/ReVancedYT/remove ]]; then
	pm uninstall com.google.android.youtube
	cmd appops set --uid com.android.vending GET_USAGE_STATS allow
	rm -rf /data/adb/service.d/YouTubeReVanced-uninstall.sh
fi

# Remove Youtube ReVanced module if YouTube app is uninstalled manually by user
PACKAGE=$(pm list packages | grep com.google.android.youtube | head -n 1 | cut -d ":" -f2-)
if [ "$PACKAGE" != "com.google.android.youtube" ]; then
	rm -rf /data/adb/modules/YouTubeReVanced
	cmd appops set --uid com.android.vending GET_USAGE_STATS allow
	rm -rf /data/adb/service.d/YouTubeReVanced-uninstall.sh
fi

