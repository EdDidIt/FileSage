import random
from typing import List
from .interpreter import InterpretedEntry, format_file_size, format_time_echo

def edwardize(structure: List[InterpretedEntry]) -> List[InterpretedEntry]:
    for entry in structure:
        entry["description"] += " — A node in the cosmic lattice."
        for file in entry["files"]:
            # Add temporal echo and cosmic weight
            size_str = format_file_size(file["size"])
            time_str = format_time_echo(file["modified"])
            
            # Enhanced description with metadata
            file["description"] += f" — {size_str} — {time_str} — " + generate_cosmic_comment(file["chaos_index"])
            
    return structure

def generate_cosmic_comment(chaos_index: float) -> str:
    """Generate Edward's cosmic commentary based on chaos index"""
    if chaos_index >= 8.0:
        return random.choice([
            "🎭 Chaos Index: %.1f — masquerades as order, but is pure entropy." % chaos_index,
            "🌪️ Chaos Index: %.1f — a vortex of digital madness." % chaos_index,
            "💀 Chaos Index: %.1f — abandon hope, all ye who debug here." % chaos_index,
            "🔥 Chaos Index: %.1f — burns with the intensity of a dying star." % chaos_index
        ])
    elif chaos_index >= 6.0:
        return random.choice([
            "🛸 Chaos Index: %.1f — may contain alien syntax and forbidden knowledge." % chaos_index,
            "🌀 Chaos Index: %.1f — swirls with the echoes of forgotten logic." % chaos_index,
            "⚡ Chaos Index: %.1f — crackles with unstable digital energy." % chaos_index,
            "🌊 Chaos Index: %.1f — waves of complexity crash against mortal understanding." % chaos_index
        ])
    elif chaos_index >= 4.0:
        return random.choice([
            "📡 Chaos Index: %.1f — transmits data to the Outernet with moderate interference." % chaos_index,
            "🌌 Chaos Index: %.1f — written during a solar flare, possibly." % chaos_index,
            "🔮 Chaos Index: %.1f — contains mysteries wrapped in enigmas." % chaos_index,
            "🎪 Chaos Index: %.1f — performs digital acrobatics with questionable grace." % chaos_index
        ])
    elif chaos_index >= 2.0:
        return random.choice([
            "✨ Chaos Index: %.1f — sparkles with contained digital harmony." % chaos_index,
            "🌸 Chaos Index: %.1f — blooms with orderly complexity." % chaos_index,
            "🎵 Chaos Index: %.1f — hums a tune of structured logic." % chaos_index,
            "🦋 Chaos Index: %.1f — flutters with elegant simplicity." % chaos_index
        ])
    else:
        return random.choice([
            "🕊️ Chaos Index: %.1f — serene as a digital meditation." % chaos_index,
            "🌿 Chaos Index: %.1f — grows in perfect algorithmic harmony." % chaos_index,
            "💎 Chaos Index: %.1f — crystalline in its structural beauty." % chaos_index,
            "🎋 Chaos Index: %.1f — stands tall with zen-like code clarity." % chaos_index
        ])
