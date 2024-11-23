import os
import json
import sys
import shutil


def generate_drum_preset(folder_path, output_file="patch.json"):
    # Validate the folder path
    if not os.path.exists(folder_path):
        print(f"Error: Folder path '{folder_path}' does not exist.")
        sys.exit(1)

    # Determine the output directory name
    folder_name = os.path.basename(os.path.normpath(folder_path))
    output_dir = os.path.join(os.path.dirname(folder_path), f"{folder_name}.preset")

    # Create the output directory
    os.makedirs(output_dir, exist_ok=True)

    # Initialize the base JSON structure
    data = {
        "engine": {
            "bendrange": 8191,
            "highpass": 0,
            "modulation": {
                "aftertouch": {"amount": 16383, "target": 0},
                "modwheel": {"amount": 16383, "target": 0},
                "pitchbend": {"amount": 16383, "target": 0},
                "velocity": {"amount": 16383, "target": 0},
            },
            "params": [16384] * 8,
            "playmode": "mono",
            "portamento.amount": 0,
            "portamento.type": 32767,
            "transpose": 0,
            "tuning.root": 0,
            "tuning.scale": 0,
            "velocity.sensitivity": 19660,
            "volume": 18348,
            "width": 0,
        },
        "envelope": {
            "amp": {"attack": 0, "decay": 0, "release": 1000, "sustain": 32767},
            "filter": {"attack": 0, "decay": 3276, "release": 23757, "sustain": 983},
        },
        "fx": {
            "active": False,
            "params": [22014, 0, 30285, 11880, 0, 32767, 0, 0],
            "type": "ladder",
        },
        "lfo": {
            "active": False,
            "params": [20309, 5679, 19114, 15807, 0, 0, 0, 12287],
            "type": "random",
        },
        "octave": 0,
        "platform": "OP-XY",
        "regions": [],
        "type": "drum",
        "version": 4,
    }

    # Valid audio file extensions
    valid_extensions = {".wav", ".aif", ".aiff"}

    # Collect all subfolders and their valid files
    folder_contents = []
    for root, dirs, files in os.walk(folder_path):
        if root == folder_path:  # Ignore the top-level directory itself
            continue
        parent_folder = os.path.basename(root)
        valid_files = [file for file in files if file.lower().endswith(tuple(valid_extensions))]
        folder_contents.append((parent_folder, valid_files))

    # Sort folders alphabetically
    folder_contents = sorted(folder_contents, key=lambda x: x[0].lower())

    # Map regions to folders and ensure 24 regions
    regions = []
    for i in range(24):
        if i < len(folder_contents):
            folder_name, files = folder_contents[i]
            sample = files[0] if files else ""  # Use the first valid file or blank
        else:
            sample = ""  # Fill remaining regions with blank samples
        regions.append(sample)

    # Build regions JSON structure
    for i, sample in enumerate(regions):
        region = {
            "fade.in": 0,
            "fade.out": 0,
            "framecount": 10000 + i * 1000,  # Placeholder value for framecount
            "hikey": 53 + i,
            "lokey": 53 + i,
            "pan": 0,
            "pitch.keycenter": 60,
            "playmode": "oneshot",
            "reverse": False,
            "sample": sample,  # File name only, no path if empty
            "sample.end": 10000 + i * 1000,  # Placeholder value for sample.end
            "transpose": 0,
            "tune": 0,
        }
        data["regions"].append(region)

    # Write the patch.json file to the output directory
    patch_file_path = os.path.join(output_dir, output_file)
    with open(patch_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    # Copy valid sample files to the output directory (flattened structure)
    for _, files in folder_contents:
        for file in files:
            file_path = os.path.join(folder_path, _, file)
            dest_path = os.path.join(output_dir, file)
            shutil.copy(file_path, dest_path)

    print(f"Drum preset created at: {output_dir}")


if __name__ == "__main__":
    # Check if the folder path is provided
    if len(sys.argv) < 2:
        print("Usage: python generate_drum_preset.py <folder_path> [output_file]")
        sys.exit(1)

    # Get folder path from arguments
    folder_path = sys.argv[1]

    # Get output file name or default to "patch.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "patch.json"

    # Run the drum preset generation function
    generate_drum_preset(folder_path, output_file)