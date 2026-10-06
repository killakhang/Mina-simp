from dataclasses import dataclass, field

@dataclass
class RelationshipState:
    rapport: float = 0.0
    trust: float = 0.0
    pressure: float = 0.0
    conflict: float = 0.0
    disengagement: float = 0.0
    boundaries: list[str] = field(default_factory=list)

    def clamp(self) -> None:
        for name in ("rapport", "trust", "pressure", "conflict", "disengagement"):
            setattr(self, name, max(0.0, min(1.0, float(getattr(self, name)))))
