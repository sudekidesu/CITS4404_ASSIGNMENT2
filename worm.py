from dataclasses import dataclass

@dataclass
class Worm:
    """Represents a single worm"""
    x: float
    y: float
    r: float
    theta: float
    d: float
    gamma: float
    width: float
    color: float

    def __post_init__(self):
        """Ensure the Bezier curve parameters are valid."""
        self.x = float(self.x)
        self.y = float(self.y)
        self.r = float(abs(self.r))
        self.theta = float(self.theta) % (2 * np.pi)
        self.d = float(abs(self.d))
        self.gamma = float(self.gamma) % (2 * np.pi)
        self.width = float(abs(self.width))
        self.color = float(self.color)