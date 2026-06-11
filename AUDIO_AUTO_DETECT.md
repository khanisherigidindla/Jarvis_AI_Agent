# 🎧 Jarvis AI - Automatic Headset Detection

## Overview

Your Jarvis AI now features **automatic headset detection**! It will automatically detect when your **Airdopes 161** headset is connected and switch to it, or use system audio when it's not connected.

**No manual configuration needed!** Just plug in your headset and Jarvis will automatically switch to it on the next startup.

---

## ✨ Features

### 🎧 Automatic Headset Detection
- **Detects Airdopes 161** when connected to your computer
- **Auto-switches to headset** for both input (microphone) and output (speakers)
- **Falls back to system audio** when headset is not connected
- **Works on every startup** - no need to configure anything!

### 🔄 Seamless Switching
- **Airdopes 161 connected?** → Jarvis uses the headset automatically
- **Airdopes 161 disconnected?** → Jarvis switches to system speakers/mic automatically

### 📝 Persistent Configuration
- **Remembers your preferences** between sessions
- **Stores configuration** in `config/audio_devices.json`
- **Easy to override** using manual controls if needed

---

## 🚀 How It Works

### On Startup
When you launch Jarvis (`python main.py`):

1. **Detects all connected audio devices**
2. **Checks for Airdopes 161 headset**
3. **If found:** Uses it for input + output 🎧
4. **If not found:** Falls back to system default audio 🔊
5. **Displays status** in console

### Example Startup Output
```
[Audio Config] 🎧 Headset 'airdopes' detected - using for audio
🎧 Airdopes 161 Headset: CONNECTED
Auto-Detect Mode: ENABLED ✓
Current Input Device: 24 (Airdopes 161)
Current Output Device: 23 (Airdopes 161)
```

Or when disconnected:
```
[Audio Config] 🎧 Headset 'airdopes' not detected - using system audio
❌ Airdopes 161 Headset: NOT CONNECTED
Auto-Detect Mode: DISABLED
Current Input Device: 1 (System Default)
Current Output Device: 4 (System Default)
```

---

## 📋 Use Cases

### Case 1: Headset Connected
**Scenario:** You plug in your Airdopes 161 and start Jarvis

✅ **What Happens:**
- Jarvis detects the headset
- Automatically switches to use Airdopes 161
- Your voice goes through the headset mic
- Jarvis's responses play through the headset speakers

### Case 2: Headset Not Connected
**Scenario:** You start Jarvis without your Airdopes 161

✅ **What Happens:**
- Jarvis detects the headset is missing
- Falls back to system microphone + system speakers
- Your voice goes through the system microphone
- Jarvis's responses play through system speakers

### Case 3: Switching During Use
**Scenario:** You're running Jarvis and plug in/unplug the headset

⚠️ **Current Behavior:** 
- Auto-detection only runs on startup
- To use a different device while Jarvis is running, use the **AUDIO DEVICES** dropdown in the UI
- On next startup, auto-detection will run again

---

## 🛠️ Using the Setup Utility

You can manually test and configure auto-detection:

```bash
python audio_setup.py
```

### Menu Options
- **[1] List all audio devices** - See all connected devices with headset status
- **[2] Test microphone** - Test recording from a device
- **[3] Test speaker** - Test playback to a device
- **[4] Configure preferred devices** - Manually select devices (overrides auto-detect)
- **[5] Auto-detect Airdopes 161** - Manually trigger auto-detection
- **[6] Check auto-detect status** - View current auto-detect mode and settings
- **[7] Exit** - Close the utility

### Example: Auto-Detect Airdopes 161

1. Run `python audio_setup.py`
2. Select option **[5]**
3. System will detect Airdopes 161
4. Devices will be saved automatically

---

## 🎯 Configuration File

Auto-detect settings are stored in: `config/audio_devices.json`

```json
{
    "selected_input_device": 24,
    "selected_output_device": 23,
    "headset_mode": true
}
```

- **selected_input_device**: ID of microphone to use
- **selected_output_device**: ID of speaker to use
- **headset_mode**: Whether Airdopes 161 was detected

---

## 🔧 Advanced Usage

### Manual Override
Even with auto-detection enabled, you can manually switch devices:

1. **While Jarvis is running:**
   - Use the **AUDIO DEVICES** section in the UI
   - Select different input/output devices from dropdowns

2. **For next startup:**
   - Run `python audio_setup.py`
   - Select **[4] Configure preferred devices**
   - Choose your devices manually

### Detect Different Headset
To detect a different headset model, modify `main.py`:

```python
# Change from:
self.audio_manager.auto_select_audio_devices("airdopes")

# To:
self.audio_manager.auto_select_audio_devices("your_headset_name")
```

---

## ❓ Troubleshooting

### Headset Not Detected
**Problem:** Airdopes 161 is connected but not detected

✅ **Solutions:**
1. Make sure Airdopes 161 is properly paired with Windows
2. Check if the device shows in `Settings > Sound > Advanced > Volume mixer`
3. Run `python audio_setup.py` → Option **[1]** to list all devices
4. Look for "Airdopes" in the device name

### Jarvis Still Using System Audio
**Problem:** Headset is connected but Jarvis uses system speakers

✅ **Solutions:**
1. Make sure you restarted Jarvis (`python main.py`)
2. Auto-detection only runs on startup
3. Check console output for auto-detect status
4. Manually select the headset using the **AUDIO DEVICES** UI dropdown

### Wrong Device Selected
**Problem:** Auto-detection picked the wrong device

✅ **Solutions:**
1. Run `python audio_setup.py`
2. Select **[4] Configure preferred devices**
3. Manually select the correct input and output devices
4. Exit and restart Jarvis

---

## 📊 How Detection Works

The system:
1. **Queries all audio devices** from Windows
2. **Searches device names** for "airdopes" (case-insensitive)
3. **Checks both input and output** of matching device
4. **Auto-assigns** the headset if both are available
5. **Falls back to system default** if headset not found
6. **Saves configuration** for next startup

---

## 🎯 Quick Commands

### Check Headset Status
```bash
python audio_setup.py
[Select option 6 - Check auto-detect status]
```

### Manually Trigger Auto-Detection
```bash
python audio_setup.py
[Select option 5 - Auto-detect Airdopes 161]
```

### List All Devices
```bash
python audio_setup.py
[Select option 1 - List all audio devices]
```

### Test Headset Mic
```bash
python audio_setup.py
[Select option 2 - Test microphone]
[Enter device number when prompted]
```

### Test Headset Speaker
```bash
python audio_setup.py
[Select option 3 - Test speaker]
[Enter device number when prompted]
```

---

## 💡 Tips & Best Practices

### Best Practice: Pair Before Starting
1. **Pair Airdopes 161** with your computer first
2. Make sure it shows in Windows Sound settings
3. **Then start Jarvis** - auto-detection will find it

### Pro Tip: Keep Headset On
- Keep Airdopes 161 paired and in range
- Jarvis will automatically switch to it on next startup if it appears

### Pro Tip: Check Status First
Before troubleshooting, always run:
```bash
python audio_setup.py
[Option 6 - Check auto-detect status]
```

---

## 📞 Support

### Verify Auto-Detection Code
```bash
python -c "from config.audio_config import get_audio_manager; m = get_audio_manager('./config'); input_dev, output_dev = m.auto_select_audio_devices('airdopes'); print(f'Input: {input_dev}, Output: {output_dev}')"
```

### View Configuration File
```bash
cat config/audio_devices.json
```

### Check Connected Devices
```bash
python audio_setup.py
[Option 1 - List all audio devices]
```

---

## 🎉 Summary

Your Jarvis AI now has **fully automatic headset detection**! 

**Just:**
1. ✅ Pair your Airdopes 161 with Windows
2. ✅ Start Jarvis with `python main.py`
3. ✅ Jarvis automatically detects and uses your headset!

**When headset not connected:**
4. ✅ Jarvis automatically switches to system audio

**No configuration needed!** Just plug and play! 🚀
