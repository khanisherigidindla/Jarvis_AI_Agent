#!/usr/bin/env python3
"""Test script for auto-detection feature."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

from config.audio_config import get_audio_manager

print("="*70)
print("JARVIS AUTO-DETECTION TEST")
print("="*70)

BASE_DIR = Path.cwd()
manager = get_audio_manager(BASE_DIR / "config")

print("\n[STARTUP] Detecting audio devices...\n")
input_dev, output_dev = manager.auto_select_audio_devices("airdopes")

print(f"[RESULT] Auto-select returned:")
print(f"  Input Device:  {input_dev}")
print(f"  Output Device: {output_dev}")

print("\n[STATUS] Checking device status:\n")
manager.print_all_devices()

print("\n✓ Auto-detection test completed successfully!")
