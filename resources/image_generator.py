#!/usr/bin/env python3
"""
Image Generator - Generates test images in various formats with random pixel data.
Supports JPG, JPEG, PNG, and HEIC formats.

Usage:
    python image_generator.py

Requirements:
    pip install Pillow numpy pillow-heif
"""

import os
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

try:
    from pillow_heif import register_heif_opener
    HEIC_AVAILABLE = True
except ImportError:
    HEIC_AVAILABLE = False
    print("Warning: pillow-heif not available. HEIC generation will create placeholder files.")


class ImageGenerator:
    """Generates various image formats with random data for testing purposes."""

    def __init__(self, output_dir="test_images"):
        self.output_dir = output_dir
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        os.makedirs(self.output_dir, exist_ok=True)

    def create_random_image(self, width=100, height=100, channels=3, label=None):
        """Create a random image with optional text label overlay."""
        random_data = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
        img = Image.fromarray(random_data)
        if label:
            img = self._add_text_overlay(img, label)
        return img

    def _add_text_overlay(self, img, text):
        """Add centered text overlay to an image."""
        draw = ImageDraw.Draw(img)
        font_size = min(img.width, img.height) // 10
        font = None
        for font_path in [
            "/System/Library/Fonts/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]:
            try:
                font = ImageFont.truetype(font_path, font_size)
                break
            except (OSError, IOError):
                continue
        if font is None:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (img.width - text_width) // 2
        y = (img.height - text_height) // 2

        for adj in range(-2, 3):
            for adj2 in range(-2, 3):
                if adj != 0 or adj2 != 0:
                    draw.text((x + adj, y + adj2), text, font=font, fill=(255, 255, 255))
        draw.text((x, y), text, font=font, fill=(0, 0, 0))
        return img

    def generate_jpg(self, filename="test_image.jpg", width=200, height=150, quality=85, label=None):
        """Generate a JPG file with random data."""
        img = self.create_random_image(width, height, label=label)
        filepath = os.path.join(self.output_dir, filename)
        img.save(filepath, "JPEG", quality=quality)
        print(f"Generated: {filename}")
        return filepath

    def generate_jpeg(self, filename="test_image.jpeg", width=150, height=200, quality=90, label=None):
        """Generate a JPEG file with random data."""
        img = self.create_random_image(width, height, label=label)
        filepath = os.path.join(self.output_dir, filename)
        img.save(filepath, "JPEG", quality=quality)
        print(f"Generated: {filename}")
        return filepath

    def generate_png(self, filename="test_image.png", width=180, height=120, label=None):
        """Generate a PNG file with random data."""
        img = self.create_random_image(width, height, label=label)
        filepath = os.path.join(self.output_dir, filename)
        img.save(filepath, "PNG")
        print(f"Generated: {filename}")
        return filepath

    def generate_heic(self, filename="test_image.heic", width=160, height=160, label=None):
        """Generate a HEIC file with random data."""
        if HEIC_AVAILABLE:
            register_heif_opener()
            img = self.create_random_image(width, height, label=label)
            filepath = os.path.join(self.output_dir, filename)
            img.save(filepath, "HEIF")
            print(f"Generated: {filename}")
            return filepath
        else:
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, "wb") as f:
                f.write(os.urandom(1024))
            print(f"Generated: {filename} (placeholder — pillow-heif not installed)")
            return filepath

    def generate_all_formats(self):
        """Generate one file in each supported format."""
        print("Generating test images in all formats...")
        files = [
            self.generate_jpg(),
            self.generate_jpeg(),
            self.generate_png(),
            self.generate_heic(),
            self.generate_jpg("large_test_image.jpg", width=800, height=600, quality=75),
            self.generate_png("small_test_image.png", width=50, height=50),
            self.generate_jpeg("medium_test_image.jpeg", width=300, height=200, quality=60),
        ]
        print(f"\nAll images generated in '{self.output_dir}/'")
        return files

    def generate_custom_images(self, count=5, format_type="jpg"):
        """Generate multiple images with random dimensions."""
        files = []
        for i in range(count):
            width = random.randint(100, 500)
            height = random.randint(100, 500)
            ext = format_type.lower()
            filename = f"custom_image_{i + 1}.{ext}"
            if ext in ("jpg",):
                files.append(self.generate_jpg(filename, width, height))
            elif ext == "jpeg":
                files.append(self.generate_jpeg(filename, width, height))
            elif ext == "png":
                files.append(self.generate_png(filename, width, height))
            elif ext == "heic":
                files.append(self.generate_heic(filename, width, height))
        return files

    def list_generated_files(self):
        """Print all files currently in the output directory."""
        if os.path.exists(self.output_dir):
            files = os.listdir(self.output_dir)
            print(f"\nFiles in '{self.output_dir}/':")
            for f in sorted(files):
                size = os.path.getsize(os.path.join(self.output_dir, f))
                print(f"  {f} ({size} bytes)")
        else:
            print(f"Output directory '{self.output_dir}' does not exist.")


# Convenience module-level functions
def generate_jpg(filename="test_image.jpg", width=200, height=150, quality=85, label=None):
    return ImageGenerator().generate_jpg(filename, width, height, quality, label)

def generate_jpeg(filename="test_image.jpeg", width=150, height=200, quality=90, label=None):
    return ImageGenerator().generate_jpeg(filename, width, height, quality, label)

def generate_png(filename="test_image.png", width=180, height=120, label=None):
    return ImageGenerator().generate_png(filename, width, height, label)

def generate_heic(filename="test_image.heic", width=160, height=160, label=None):
    return ImageGenerator().generate_heic(filename, width, height, label)

def generate_all_images():
    return ImageGenerator().generate_all_formats()


if __name__ == "__main__":
    print("Image Generator — creating test images with random data")
    print("=" * 60)
    generator = ImageGenerator()
    generator.generate_all_formats()
    print("\nGenerating custom images...")
    generator.generate_custom_images(3, "jpg")
    generator.generate_custom_images(2, "png")
    generator.list_generated_files()
