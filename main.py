#!/usr/bin/env python3
"""Writes the robot wedding vow to /output/entry.txt."""

import os

# One-line robot wedding vow (88 characters).
VOW = "I promise to love you, honor you, and never update my firmware without asking you first."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(VOW)
