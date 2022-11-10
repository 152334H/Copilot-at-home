# Running this backend
Assumes a debian-like Linux installation with anaconda.
```bash
conda create --name fakecopilot python=3.9
conda env update -n fakecopilot --file environment.yaml
conda activate fakecopilot
python app.py
```

You can also run `python code.py` to generate code from the terminal.

## I don't have anaconda
The required packages are essentially `faiss-gpu`, `pytorch==1.13`, `transformers>=4.24`, and `flask`. `faiss-gpu` is unfortunately not pip installable directly.

## Hardware requirements
Loading the model causes an immediate spike in RAM to slightly &gt;16GB. This can probably be fixed.

The model requires slightly more than 6GB of vram to run right now. If that is too much, you can experiment by changing:
```python
MODEL_NAME = "Salesforce/codegen-2B-mono"
```
to
```python
MODEL_NAME = "Salesforce/codegen-350M-mono"
```
But this will naturally perform much more poorly. You could also modify the code to use one of the smaller PolyCoder models.

The `-mono` model can also be switched to `-multi` for non-python languages.

## Bugs
This code was written in two hours so please report any bugs
