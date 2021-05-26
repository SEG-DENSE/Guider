# GUIDER

An automated Android GUI test script repair tool that utilizes both structural and visual information in app GUIs.

## I. Requirement

- [Appium 1.0.2](https://github.com/appium/appium-desktop/releases/tag/v1.0.2-beta.2)
- [Android SDK](https://developer.android.com/studio)
- Android phone or Emulator (Android 7.0 or higher)

## II. Run the Service of Appium

You just need to start a service by default in Appium.

## III. Connect Android Phones and the Computer

1. Connect your phones via the USB line. You can also use the Android emulator instead.
2. In the terminal, execute `adb devices` to make sure that the phone is connected.

## IV. Run GUIDER

1. Create the root directory, e.g., `/Users/nju/Documents/issta-artifact/`, and then `git clone https://github.com/SEG-DENSE/Guider`. Make sure that `ApkTestScript` is under the root directory.

2. Given an app, record the dynamic testing results (including images and layout files) of the base version with the command `Main/Main -a <App_Name> -c <Script_Name> -r <Root_Path> -o <Based_Version_Path> -n <Updated_Version_Path> -v <Based_Phone_Version> -w <Updated_Phone_Version> -p <App_Package> -t <App_Activity> -l <Repair_Strategy>`

   - Example: `Main/Main -a 'google driver 1' -c 'google driver 1' -r /Users/nju/Documents/issta-artifact/ -o /Users/nju/Desktop/apk/app-fdroid-debug-old.apk -n /Users/nju/Desktop/apk/app-fdroid-debug-new.apk -v 7.0 -w 10 -p 'com.google.android.apps.docs' -t 'com.google.android.apps.docs.app.NewMainProxyActivity' -l guider`
   - Explaination: The parameter `-a` represents the app is named as `google driver 1`, the parameter `-c` represents the script is named as `google driver 1.py`, the parameter `-v` represents the android version of the phone used to test the base version app (7.0 in this example), the parameter `-w` represents the android version of the phone used to test the updated app (10 in this example), and the parameter `-l` represents the repair strategy to apply (water, meter and guider).

3. For the updated version, repair the broken test action.

   When the recording process finishes, install the updated version apk in the phone, or just switch to another phone, where the updated version apk has been installed.

   After the updated version app has been installed, press the Enter button in the keyboard to start the repair process.


## V. Structure of the Directories

```
 |--- README.md               :  readme file
 |--- ApkTestScript           :  broekn test scripts of the updated version app
 |--- apk                     :  apk files of both the base and updated versions of the apps
 |--- Results                 :  experiment results 
 |--- guider_output           :  outputs of Guider strategy
 |----meter_output            :  outputs of Meter strategy
 |----water_output            :  outputs of Water strategy
 |----Main            	      :  executable file 
```

