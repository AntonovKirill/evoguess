from .interval import *
from .backdoor import *

types = {
    Interval.slug: Interval,
    Backdoor.slug: Backdoor,
}

backdoors = {
    Backdoor.slug: Backdoor
}

for kind, backdoor in enumerate(backdoors.values()):
    setattr(backdoor, 'kind', kind)

__all__ = [
    'Interval',
    'Backdoor'
]
