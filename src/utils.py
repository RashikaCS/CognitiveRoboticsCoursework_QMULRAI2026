def target_label(value):
    """
    Convert numeric prediction to human-readable label
    """
    if value == 0:
        return "Small Object"
    elif value == 1:
        return "Large Object"
    else:
        return "Unknown"


def cue_label(value):
    """
    Convert numeric cue to readable label
    """
    if value == 0:
        return "small"
    elif value == 1:
        return "large"
    else:
        return "unknown"