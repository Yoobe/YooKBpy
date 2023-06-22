from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC

SAY_HI = simple_key_sequence(
    (
        KC.T,
        KC.MACRO_SLEEP_MS(100),
        KC.H,
        KC.I,
        KC.MACRO_SLEEP_MS(100),
        KC.ENTER,
        KC.MACRO_SLEEP_MS(100),
    )
)