# OP-XY-drum-preset-builder
Build drum sampler presets from a list of files.


## Use
1. Install python if you havent already
2. Download this repository and place it somewhere for easy access.
3. Create a new folder with your desired name for your drum preset
4. Unzip the "blank_sample_sots.zip" file. Copy all of the sub-folders within it and paste them into the new folder you just created.
5. Find the samples you want to add to your OP-XY and place one of them in each folder (similar to how you would do on the op-z). The folders correspond to the keys on the OP-XY's keyboard, so "__f" is the first key and "e" is the last key.
6. In your terminal run the following
```
python generate_drum_preset.py <path_to_preset_folder>
```
7. It should output a folder called <name_of_your_preset>.preset, with all of your original samples and a file called `patch.json`.
8. Connect your OP-XY to your computer using mtp/field-kit. Drop the <name_of_your_preset>.preset folder into the `presets/user` folder on your OP-XY.
9. Eject the OP-XY.
10. Hit shift + instrument track and navigate to the user folder. Open up your new preset!


## Known Bugs
One thing I know is a bit weird is that this spript does properly set the loop end point for samples. This is pretty quick to fix (just twist the light grey knob if you notice it). I'm sure there's a way to get this scrip to set the propper framecount and loop end, but I'm not sure how to do that.

I used ChatGPT to write this. I'm audited the code a bit, but I'm not a seasoned python developer, so if there are bugs or inefficiency, I appoligize! I probably wont be able to help you troubleshoot much. If you have suggestions though, feel free to submit a pull request.

It would be great if we could create an interface to modify the other parameters in the JSON in a way that made sense. For now though this will hopefully allow you to quickly build drumkits.
