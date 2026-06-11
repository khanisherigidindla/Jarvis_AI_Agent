# ⚡ Quick Reference - Audio Device Setup

## 3-Step Quick Start

```bash
# Step 1: Run the setup utility
python audio_setup.py

# Step 2: Select option [1] to see your devices
# Step 3: Select option [4] to configure
# Step 4: Run Jarvis
python main.py
```

## What You'll See

### In `python audio_setup.py` (Option 1):

```
📥 INPUT DEVICES (Microphones):
  [0] Microphone (System)          (2 ch)  microphone   ✓ DEFAULT
  [1] Headset Microphone (USB)     (1 ch)  headset
  
📤 OUTPUT DEVICES (Speakers):
  [0] Speakers (System)            (2 ch)  speaker      ✓ DEFAULT
  [1] Headphones (USB)             (2 ch)  headset
```

### In Jarvis UI:

```
AUDIO DEVICES
📥 INPUT: [Dropdown with all microphones]
📤 OUTPUT: [Dropdown with all speakers]
```

## Common Commands

| Task | Command |
|------|---------|
| List all devices | `python audio_setup.py` → Option 1 |
| Test microphone | `python audio_setup.py` → Option 2 |
| Test speaker | `python audio_setup.py` → Option 3 |
| Configure devices | `python audio_setup.py` → Option 4 |
| Run Jarvis | `python main.py` |
| Switch device | Use dropdown in Jarvis UI |

## Device Number Reference

- Device [0], [1], [2] etc. = Device ID
- These numbers are from `sounddevice` library
- Write down your preferred device numbers!

## File Locations

| File | Purpose |
|------|---------|
| `config/audio_config.py` | Device manager (new) |
| `audio_setup.py` | Setup utility (new) |
| `config/audio_devices.json` | Saved preferences (auto-created) |
| `AUDIO_SETUP.md` | Detailed guide |
| `main.py` | Updated for audio devices |
| `ui.py` | Updated with device dropdowns |

## Troubleshooting Quick Links

| Issue | Solution |
|-------|----------|
| No devices show up | Run Option 1 in setup, plug in device, retry |
| Microphone not working | Run Option 2 in setup to test |
| No audio output | Run Option 3 in setup to test |
| Device not available | Check Windows Sound Settings |

## Important Notes

⚠️ **Before you start:**
- Make sure your microphone/headset is plugged in
- Check Windows Volume Control
- All dependencies are already in `requirements.txt`

✅ **After setup:**
- You can switch devices anytime in UI
- Settings are saved automatically
- If device unplugged, Jarvis falls back to default

📌 **Pro Tip:** 
Save the device numbers you want to use! Example:
- Input: Device [1] (Headset Mic)
- Output: Device [1] (Headset Speakers)

## Most Common Setup

**For Headset Users:**
```
1. Run: python audio_setup.py
2. Choose: 1 (list devices)
3. Note: Headset device number
4. Choose: 4 (configure)
5. Enter: Headset device number for input
6. Enter: Headset device number for output
7. Done!
```

**For System Audio Only:**
```
1. Run: python audio_setup.py
2. Choose: 4 (configure)
3. Press: Enter for all prompts (use defaults)
4. Done!
```

## One-Liner Test

```bash
python -m py_compile config/audio_config.py audio_setup.py main.py ui.py && echo "✓ All files ready!"
```

## Need Help?

1. **Check:** `AUDIO_SETUP.md` (detailed guide)
2. **Run:** `python audio_setup.py` (interactive help)
3. **Read:** `AUDIO_IMPLEMENTATION_COMPLETE.md` (overview)
4. **Console:** Look for error messages when running Jarvis

---

**Ready?** Start with: `python audio_setup.py`
