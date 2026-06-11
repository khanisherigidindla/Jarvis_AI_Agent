#!/usr/bin/env python3
"""
Audio Device Setup Utility for Jarvis AI

This script helps you detect, list, and configure audio devices
for both headset and system speaker input/output.

Run this script to:
1. See all available audio devices
2. Test microphone input
3. Test speaker output  
4. Configure which devices to use
"""

import sys
import time
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent))

import sounddevice as sd
from config.audio_config import get_audio_manager


def separator(title: str = ""):
    """Print a formatted separator line."""
    if title:
        print(f"\n{'='*70}")
        print(f"  {title}")
        print(f"{'='*70}\n")
    else:
        print(f"\n{'-'*70}\n")


def list_devices():
    """List all available audio devices."""
    separator("AVAILABLE AUDIO DEVICES")
    
    manager = get_audio_manager(Path(__file__).parent / "config")
    
    print("📥 INPUT DEVICES (Microphones):\n")
    input_devices = manager.get_all_input_devices()
    if not input_devices:
        print("  ❌ No input devices found!")
    else:
        for dev in input_devices:
            default = "✓ DEFAULT" if dev["default_input"] else ""
            print(f"  [{dev['id']}] {dev['name']:<40} ({dev['channels']} ch)  {dev['type']:<12}  {default}")
    
    print("\n📤 OUTPUT DEVICES (Speakers):\n")
    output_devices = manager.get_all_output_devices()
    if not output_devices:
        print("  ❌ No output devices found!")
    else:
        for dev in output_devices:
            default = "✓ DEFAULT" if dev["default_output"] else ""
            print(f"  [{dev['id']}] {dev['name']:<40} ({dev['channels']} ch)  {dev['type']:<12}  {default}")
    
    print()
    return manager, input_devices, output_devices


def test_microphone(manager, device_id: int):
    """Test recording from a microphone device."""
    print(f"\n🎤 Testing microphone (Device {device_id})...")
    print("   Recording 3 seconds... Please speak into the microphone.\n")
    
    try:
        import numpy as np
        
        duration = 3
        samplerate = 16000
        
        # Record audio
        audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, device=device_id)
        sd.wait()
        
        # Check if any sound was detected
        max_level = float(np.max(np.abs(audio_data)))
        
        print(f"   ✓ Recording complete!")
        print(f"   Signal level: {max_level:.4f} (normalized)")
        
        if max_level < 0.01:
            print(f"   ⚠️  Very low signal - microphone might not be working or is muted")
        elif max_level < 0.1:
            print(f"   ⚠️  Signal is quite low - consider adjusting microphone volume")
        else:
            print(f"   ✓ Good signal level detected!")
        
        return True
    except Exception as e:
        print(f"   ❌ Error testing microphone: {e}")
        return False


def test_speaker(device_id: int):
    """Test playback to a speaker device."""
    print(f"\n🔊 Testing speaker (Device {device_id})...")
    print("   Playing 1-second test tone... You should hear a beep.\n")
    
    try:
        import numpy as np
        
        duration = 1
        samplerate = 24000
        frequency = 440  # A4 note
        
        # Generate sine wave
        t = np.linspace(0, duration, int(samplerate * duration))
        audio_data = np.sin(2 * np.pi * frequency * t) * 0.3  # 30% volume
        
        # Play audio
        sd.play(audio_data, samplerate=samplerate, device=device_id)
        sd.wait()
        
        print("   ✓ Playback complete! Did you hear a beep?")
        return True
    except Exception as e:
        print(f"   ❌ Error testing speaker: {e}")
        return False


def configure_devices(manager):
    """Interactive device configuration."""
    separator("CONFIGURE AUDIO DEVICES")
    
    input_devices = manager.get_all_input_devices()
    output_devices = manager.get_all_output_devices()
    
    if input_devices:
        print("Select INPUT device (microphone):")
        for dev in input_devices:
            print(f"  [{dev['id']}] {dev['name']} ({dev['type']})")
        
        while True:
            try:
                choice = input("\nEnter device number (or press Enter for default): ").strip()
                if choice == "":
                    print("  Using system default")
                    break
                dev_id = int(choice)
                if any(dev['id'] == dev_id for dev in input_devices):
                    manager.set_input_device(dev_id)
                    selected = next(dev for dev in input_devices if dev['id'] == dev_id)
                    print(f"  ✓ Selected input device: {selected['name']}")
                    break
                else:
                    print("  ❌ Invalid device number")
            except ValueError:
                print("  ❌ Please enter a valid number")
    
    if output_devices:
        separator()
        print("Select OUTPUT device (speaker/headphones):")
        for dev in output_devices:
            print(f"  [{dev['id']}] {dev['name']} ({dev['type']})")
        
        while True:
            try:
                choice = input("\nEnter device number (or press Enter for default): ").strip()
                if choice == "":
                    print("  Using system default")
                    break
                dev_id = int(choice)
                if any(dev['id'] == dev_id for dev in output_devices):
                    manager.set_output_device(dev_id)
                    selected = next(dev for dev in output_devices if dev['id'] == dev_id)
                    print(f"  ✓ Selected output device: {selected['name']}")
                    break
                else:
                    print("  ❌ Invalid device number")
            except ValueError:
                print("  ❌ Please enter a valid number")


def main():
    """Main menu."""
    separator("JARVIS AUDIO DEVICE SETUP")
    print("Welcome! This utility helps you configure audio devices for Jarvis AI.")
    print("You can use both headset and system speakers without any additional configuration.")
    print("🎧 Auto-detect mode: Automatically switches to Airdopes 161 if connected!\n")
    
    manager = get_audio_manager(Path(__file__).parent / "config")
    
    while True:
        print("\nWhat would you like to do?")
        print("  [1] List all audio devices (with headset status)")
        print("  [2] Test microphone")
        print("  [3] Test speaker")
        print("  [4] Configure preferred devices (manual)")
        print("  [5] Auto-detect Airdopes 161 headset")
        print("  [6] Check auto-detect status")
        print("  [7] Exit\n")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            manager, input_devs, output_devs = list_devices()
        
        elif choice == "2":
            try:
                manager, input_devs, output_devs = list_devices()
                if not input_devs:
                    print("❌ No input devices available!")
                    continue
                device_id = int(input("\nEnter device number to test: "))
                if any(dev['id'] == device_id for dev in input_devs):
                    test_microphone(manager, device_id)
                else:
                    print("❌ Invalid device number!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "3":
            try:
                manager, input_devs, output_devs = list_devices()
                if not output_devs:
                    print("❌ No output devices available!")
                    continue
                device_id = int(input("\nEnter device number to test: "))
                if any(dev['id'] == device_id for dev in output_devs):
                    test_speaker(device_id)
                else:
                    print("❌ Invalid device number!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "4":
            configure_devices(manager)
            print("\n✓ Configuration saved!")
        
        elif choice == "5":
            # Auto-detect headset
            print("\n🔍 Detecting Airdopes 161 headset...")
            input_dev, output_dev = manager.auto_select_audio_devices("airdopes")
            
            if input_dev is not None and output_dev is not None:
                print("\n✓ SUCCESS! Airdopes 161 detected and configured!")
                print(f"  📥 Input Device:  [{input_dev}]")
                print(f"  📤 Output Device: [{output_dev}]")
                print("\n🎧 Next time you start Jarvis, it will automatically use your Airdopes 161!")
            else:
                print("\n❌ Airdopes 161 not detected.")
                print("   Please connect your Airdopes 161 headset and try again.")
        
        elif choice == "6":
            # Check auto-detect status
            separator("AUTO-DETECT STATUS")
            manager.print_all_devices()
        
        elif choice == "7":
            print("\n✓ Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-7")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✓ Setup cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
