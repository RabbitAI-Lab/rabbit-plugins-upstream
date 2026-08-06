---
name: anthropomorphic-agent-engine
slug: anthropomorphic-agent-engine
version: 1.1.0
displayName: Anthropomorphic Agent Engine
description: Breathe life into AI agents with a deterministic psychology engine — eight-dimensional emotions that flow and linger, trauma that shapes memory, trust that erodes over time. No black boxes, no randomness, just reproducible personalities that feel profoundly human.
required_commands:
  - python3
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "🤖"
    homepage: "https://github.com/NOHN-AI/Anthropomorphic-Agent-Engine"
---
# Anthropomorphic Agent Engine
A deterministic psychological engine built on SPL Pure Core V8.0 — no probabilistic black boxes, no hidden randomness. Every state change is traceable and reproducible, giving AI agents the emotional depth needed for long-term, credible human interaction.
## Trigger Scenarios
Automatically activates when users ask about:
- Anthropomorphic agent architecture and personality implementation
- Emotion, cognition, or motivation modeling approaches
- Long-term agent behavior consistency design
- Auditable, black-box-free psychological simulation
- Novel or game character behavior deduction
## Core Capabilities
### SPL Pure Core V8.0 Architecture
- 8-dimensional emotion fluid model: joy, anger, fear, trust, alienation, tension, guilt, shame — continuous dynamic evolution
- Trauma & memory system: trauma nodes, memory reconsolidation, Ebbinghaus forgetting curve, repression-rebound mechanisms
- Trust & relationship model: trust capacity erosion under prolonged cold treatment, dynamic relationship depth calculation
- Psychological metabolism: arousal, dynamic viscosity, psychological time, energy-fatigue metabolism, sleep-dream processing
- V8.0 extensions: slow-variable emotion layer, independent shame dimension, self-esteem dynamics, expectation system (hope/anxiety/disappointment), cognitive dissonance, defense mechanisms
### Modular Extensibility
- Narrative mapping layer: customizable personalities (optimist/paranoid/nihilist) that convert external events into interoceptive vectors
- Identity engine: multi-identity model with automatic baseline tension injection on identity conflict
- Pluggable modules: goals, values, cognitive biases, and world models are independently replaceable
## Usage
### Running the Core Engine
```python
from scripts.SPL_anthropic_engine import SPLPureCoreV8_0
core = SPLPureCoreV8_0()
# Input event vector: belonging 0.5, threat -0.1, time step 1.0
core.process_vector({"belonging": 0.5, "threat": -0.1}, 1.0)
# Get complete state snapshot
print(core.snapshot())
```
### Custom Personality Configuration
```python
from assets.feature.Identity_module import IdentityEngine
identity = IdentityEngine()
identity.add_identity("poet", {"sensitivity": 0.9, "rationality": 0.3})
```
## Technical Notes
- Pure Python standard library, no extra dependencies, Python >= 3.8
- Fully deterministic: identical inputs always produce identical outputs, zero randomness
## License
Personal non-commercial research use only. Government/enterprise commercial use requires written authorization.
