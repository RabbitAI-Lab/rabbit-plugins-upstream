## Description:

Translates one SRT, VTT, or ASS subtitle file at a time while preserving timelines, validating batch mappings, and safely composing local outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lumen01](https://clawhub.ai/user/lumen01)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to translate individual subtitle files with local parsing, validation, and output composition while keeping timing and supported subtitle structure intact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional visualizer stores local task history and exposes a bridge API on 127.0.0.1 while running.

Mitigation: Run the visualizer only when live progress is needed, keep it bound to loopback, and stop the service when the local access surface is no longer needed.

Risk: The workflow writes work files, subtitle outputs, and reports on the local machine.

Mitigation: Use deliberate work and output locations, inspect generated reports, and use overwrite flags only when replacing the exact existing output is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lumen01/skills/agent-subtitle-translator)
- [Publisher Profile](https://clawhub.ai/user/lumen01)
- [Server-Resolved GitHub Source](https://github.com/Lumen01/agent-subtitle-translator)
- [README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands; generated subtitle files and JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one subtitle input per run and writes validated local outputs without requiring an external LLM API key.]

## Skill Version(s):

1.0.9 (source: server release metadata; package.json reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
