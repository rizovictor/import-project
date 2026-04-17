#!/usr/bin/env python3
"""
Main module demonstrating the import of the Shark class from the vertebrates package
"""

from vertebrates.cold_blooded.fish import Shark

print("\n--- Shark Attributes ---")
print(f"Has scales: {Shark.has_scales}")
print(f"Has fins: {Shark.has_fins}")
print(f"Breathes through gills: {Shark.breathes_through_gills}")
