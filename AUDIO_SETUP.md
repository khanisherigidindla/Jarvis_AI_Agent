# 🎤 Jarvis AI - Audio Device Configuration Guide

## Overview
Your Jarvis AI project has been updated to support **multiple audio devices**. You can now use:
- ✓ **Headset with microphone** (wired or wireless)
- ✓ **System microphone** (built-in or external)
- ✓ **Headphones/Earbuds** for output
- ✓ **System speakers** for output

All at the same time, with easy switching!

---

## Quick Start - What Changed?

### 1. **New Audio Device Manager** 📁
   - `config/audio_config.py` - Manages device detection and selection
   - `config/audio_devices.json` - Stores your preferred devices

### 2. **Updated Main Application**
   - `main.py` - Now uses the audio device manager
   - Smart device fallback system if default device is disconnected
   - Automatic device detection and switching

### 3. **Enhanced UI**
   - New "AUDIO DEVICES" section in the left panel
   - Dropdown menus to switch input/output devices in real-time
   - Device name and type display

### 4. **Setup Utility**
   - `audio_setup.py` - Interactive setup tool
   - List all devices
   - Test microphone input
   - Test speaker output
   - Configure preferred devices

---

## Setup Instructions

### Step 1: Verify Requirements ✓
All packages are already in `requirements.txt`. Make sure they're installed:

```bash
pip install -r requirements.txt
```

**Key packages for audio:**
- `sounddevice` - Audio input/output
- `numpy` - Audio data processing
- `pyqt6` - UI components

### Step 2: Run the Audio Setup Utility
This tool will help you identify and configure your devices:

```bash
python audio_setup.py
```

**What you'll see:**
```
======================================================================
  JARVIS AUDIO DEVICE SETUP
======================================================================

📥 INPUT DEVICES (Microphones):

  [0] Microphone (Realtek High Definition Audio)  (2 ch)  microphone   ✓ DEFAULT
  [1] Headset Microphone (USB Audio Device)       (1 ch)  headset
  [2] Line In (Realtek High Definition Audio)     (2 ch)  microphone

📤 OUTPUT DEVICES (Speakers):

  [0] Speakers (Realtek High Definition Audio)    (2 ch)  speaker     ✓ DEFAULT
  [1] Headphones (USB Audio Device)               (2 ch)  headset
  [2] HDMI Audio                                  (2 ch)  speaker
```

### Step 3: Test Your Devices
From the setup utility menu, select **"Test microphone"** and **"Test speaker"**:

```
[2] Test microphone
→ Enter device number to test: 1
   🎤 Testing microphone (Device 1)...
   Recording 3 seconds... Please speak into the microphone.
   ✓ Recording complete!
   Signal level: 0.4523 (normalized)
   ✓ Good signal level detected!
```

### Step 4: Configure Preferred Devices
From the setup utility menu, select **"Configure preferred devices"**:

```
[4] Configure preferred devices

Select INPUT device (microphone):
  [0] Microphone (Realtek High Definition Audio) (microphone)
  [1] Headset Microphone (USB Audio Device) (headset)
  [2] Line In (Realtek High Definition Audio) (microphone)

Enter device number (or press Enter for default): 1
  ✓ Selected input device: Headset Microphone (USB Audio Device)

Select OUTPUT device (speaker/headphones):
  [0] Speakers (Realtek High Definition Audio) (speaker)
  [1] Headphones (USB Audio Device) (headset)
  [2] HDMI Audio (speaker)

Enter device number (or press Enter for default): 1
  ✓ Selected output device: Headphones (USB Audio Device)

✓ Configuration saved!
```

### Step 5: Launch Jarvis and Switch Devices
Start Jarvis normally:

```bash
python main.py
```

In the Jarvis UI, you'll see the **AUDIO DEVICES** section with two dropdown menus:
- **📥 INPUT**: Select your preferred microphone
- **📤 OUTPUT**: Select your preferred speaker

**Switch devices anytime** - even while Jarvis is running! ⚡

---

## Device Detection 🔍

The system automatically detects device types:

| Device Type | Examples | Input/Output |
|------------|----------|--------------|
| **Headset** | USB Headset, Wireless Headphones, AirPods | Both |
| **Microphone** | Built-in Mic, Condenser Mic, Line In | Input |
| **Speaker** | Built-in Speakers, USB Speaker, HDMI Audio | Output |
| **Unknown** | Unidentified devices | Either |

---

## How It Works Behind the Scenes 🔧

### Audio Device Selection Logic

1. **Check Saved Preference**
   - If you set a preferred device, it uses that
   - Stored in `config/audio_devices.json`

2. **Fallback to System Default**
   - If saved device not available, uses Windows/system default
   - Handles disconnection gracefully (e.g., headset unplugged)

3. **Emergency Fallback**
   - If no default, finds first available device
   - Keeps Jarvis running even if devices change

### Example Scenarios

**Scenario 1: You plug in a headset**
- Jarvis automatically detects it
- You can select it from the dropdown
- Previous settings are saved

**Scenario 2: You unplug headset mid-conversation**
- Jarvis falls back to next available device
- Audio continues without interruption
- No restart needed

**Scenario 3: You switch between two devices**
- Select from the UI dropdowns
- Next recording/playback uses new device
- Instant switching!

---

## Configuration Files 📄

### `config/audio_devices.json`
Stores your device preferences:

```json
{
    "selected_input_device": 1,
    "selected_output_device": 1
}
```

**Note:** You don't need to edit this manually - use the setup utility or UI dropdowns!

### `config/api_keys.json`
Your existing config (unchanged):

```json
{
    "gemini_api_key": "your-key-here",
    "os_system": "windows"
}
```

---

## Troubleshooting 🔧

### Problem: "No input audio device detected"
**Solution:**
1. Run `audio_setup.py` to check available devices
2. Plug in microphone or headset
3. Restart Jarvis
4. Configure devices using the setup utility

### Problem: Microphone not working
**Solution:**
1. Check Windows Settings → Sound
2. Ensure microphone is not muted
3. Test with `audio_setup.py` → Option 2 (Test microphone)
4. Select the correct device from Jarvis UI

### Problem: No sound output
**Solution:**
1. Check Windows Settings → Sound
2. Ensure speakers/headphones are not muted
3. Test with `audio_setup.py` → Option 3 (Test speaker)
4. Select the correct device from Jarvis UI

### Problem: Device switching not working
**Solution:**
1. Restart Jarvis application
2. Run `audio_setup.py` to re-detect devices
3. Manually select device from UI
4. Check that device is actually connected

### Problem: Getting error messages about devices
**Solution:**
- Look at console output (Windows Command Prompt)
- Check device numbers in `audio_setup.py` output
- Verify device has required channels (input needs input channels, output needs output channels)
- Try unplugging and replugging device

---

## Advanced Usage 🚀

### Manual Device Configuration
Edit `config/audio_devices.json` directly:

```json
{
    "selected_input_device": 0,
    "selected_output_device": 0
}
```

### Using Only System Audio (No Headset)
1. Run `audio_setup.py`
2. Select "Configure preferred devices"
3. Choose only system microphone and speakers
4. Leave as default (press Enter)

### Using Only Headset
1. Plug in your headset
2. Run `audio_setup.py`
3. Configure to use headset microphone and headphones
4. Jarvis will default to headset when available

### Testing Before Running Jarvis
```bash
# List all devices
python audio_setup.py  # Choose option 1

# Test microphone
python audio_setup.py  # Choose option 2

# Test speaker
python audio_setup.py  # Choose option 3
```

---

## What's New in the Code 📝

### New Module: `config/audio_config.py`
- `AudioDeviceManager` class for device management
- `get_audio_manager()` factory function
- Automatic device type detection
- Device persistence

### Updated: `main.py`
- Imports audio config manager
- `JarvisLive` class now has:
  - `get_input_devices_list()` - Get available microphones
  - `get_output_devices_list()` - Get available speakers
  - `set_input_device_by_name()` - Change microphone
  - `set_output_device_by_name()` - Change speaker
  - `print_audio_devices()` - Debug output

### Updated: `ui.py`
- Added QComboBox imports
- New device selection dropdowns
- `_on_input_device_changed()` callback
- `_on_output_device_changed()` callback
- `update_device_lists()` method
- `set_jarvis()` method to link UI with audio manager

### New: `audio_setup.py`
- Interactive device configuration utility
- Device listing and testing
- Microphone and speaker testing
- Device preference saving

---

## Performance Considerations ⚡

✓ **Efficient** - Device detection only happens at startup
✓ **Low Overhead** - No impact on audio quality
✓ **Responsive** - Device switching is instant
✓ **Reliable** - Fallback system prevents crashes

---

## File Structure 📁

```
Jarvis_AI/
├── config/
│   ├── __init__.py
│   ├── api_keys.json              (existing)
│   ├── audio_devices.json         (new - auto-created)
│   └── audio_config.py            (new - device manager)
├── main.py                        (updated)
├── ui.py                          (updated)
├── audio_setup.py                 (new - setup utility)
└── requirements.txt               (existing - all deps included)
```

---

## Next Steps 🎯

1. ✅ **Install dependencies:** `pip install -r requirements.txt`
2. ✅ **Run setup utility:** `python audio_setup.py`
3. ✅ **Test your devices:** Options 2 and 3 in setup utility
4. ✅ **Configure preferences:** Option 4 in setup utility
5. ✅ **Launch Jarvis:** `python main.py`
6. ✅ **Switch devices:** Use dropdowns in the "AUDIO DEVICES" section

---

## Support 🆘

If you encounter issues:

1. Check the console output for error messages
2. Run `audio_setup.py` to diagnose
3. Verify Windows audio settings
4. Ensure device drivers are up to date
5. Try unplugging and replugging device

---

## Key Features Summary ✨

✅ Support for multiple microphones (headset + system)
✅ Support for multiple speakers (headset + system)
✅ Real-time device switching in UI
✅ Automatic fallback if device disconnects
✅ Persistent device preferences
✅ Easy setup utility with testing
✅ Graceful error handling
✅ No impact on existing features

---

**Your Jarvis AI is now fully configured for flexible audio input/output!** 🎉

Start with `python audio_setup.py` to get your devices set up, then `python main.py` to run Jarvis!
