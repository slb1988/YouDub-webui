# instantiate the model
import os

from pyannote.audio import Model
model = Model.from_pretrained(
  "pyannote/segmentation-3.0",
  use_auth_token=os.getenv('HF_TOKEN'))
print(model)