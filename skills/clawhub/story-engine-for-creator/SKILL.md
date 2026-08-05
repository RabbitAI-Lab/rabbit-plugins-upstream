---
name: story-engine-for-creator
slug: story-engine-for-creator
version: 1.1.0
displayName: Story Causal Engine
description: Forge epic narratives with deterministic causal reasoning — detect every plot hole, align every timeline, and let no logical gap slip through your world-building. A second-perspective engine that audits stories like a detective reviews evidence.
required_commands:
  - python3
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "✍️"
    homepage: "https://github.com/NOHN-AI/story-engine"
---
# Story Causal Engine
A deterministic narrative architecture tool for epic novels, game scripts, and screenplays — providing full-pipeline logic validation and generation from outline to final draft.
## Trigger Scenarios
Automatically activates when users ask about:
- Novel, screenplay, or game narrative architecture design
- World-building generation and consistency validation
- Plot logic hole detection and repair
- Character behavior consistency auditing
- Multi-thread narrative timeline alignment
- Pacing optimization and scene detail completion
## Core Capabilities
### Second-Perspective Causal Reasoning Core
- Natural-language outlines auto-converted into auditable causal chains
- Automatic plot logic hole detection with repair suggestions
- Full-chain character behavior consistency validation
- Multi-thread narrative timeline auto-alignment
### World-Building & Validation
- Rule-based fictional world auto-generation
- Setting conflict auto-auditing
- Power system balance validation
- Historical timeline self-consistency verification
### Story Generation & Rendering
- Multilingual story bridging and localization
- Scene detail auto-completion
- Dialogue style consistency preservation
- Narrative pacing auto-optimization
## Usage
```python
from scripts.story_engine import UltimateCausalNovelEngine
engine = UltimateCausalNovelEngine()
engine.load_worldview("path/to/your/worldview.md")
engine.parse_outline("path/to/your/outline.md")
audit_result = engine.audit_logic()
print(audit_result)
full_story = engine.generate_full_story()
```
## Typical Scenarios
1. **Epic Novel Creation**: Million-word world-building validation, plot deduction, and logic auditing
2. **Game Script Development**: Multi-branch narrative consistency checks and ending plausibility
3. **Screenplay Writing**: Pacing optimization and character logic validation
4. **IP Derivative Works**: Ensuring spin-off consistency with original world and characters
## Technical Highlights
- No black-box probability: all results traceable through complete causal chains
- Audit trail: every modification and decision leaves a verifiable record
- Fully local: no network required, all data stays on your machine
- Zero learning curve: natural language input, no markup required
## License
Personal non-commercial research use only. Commercial use requires written authorization.
