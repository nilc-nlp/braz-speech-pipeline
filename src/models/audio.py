from pydantic import BaseModel
from typing import Tuple
import numpy as np


class Audio(BaseModel):
    """
    Class to represent an audio file
    """

    name: str
    bytes: np.ndarray
    sample_rate: int
    # channels: int
    non_silent_interval: np.ndarray

    @property
    def duration(self) -> float:
        return len(self.bytes) / self.sample_rate

    @property
    def channels(self) -> int:
        return self.bytes.shape[1]

    @property
    def is_mono(self) -> bool:
        return self.channels == 1

    @property
    def trimmed_audio(self) -> np.ndarray:
        return self.bytes[self.non_silent_interval[0] : self.non_silent_interval[1]]

    @property
    def start_offset_trimmed_audio(self) -> float:
        return self.non_silent_interval[0] / self.sample_rate

    @property
    def end_offset_trimmed_audio(self) -> float:
        return self.non_silent_interval[1] / self.sample_rate