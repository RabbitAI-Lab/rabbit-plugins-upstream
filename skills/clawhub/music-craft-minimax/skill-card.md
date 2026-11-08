## Description:

Deprecated MiniMax music skill for cover and style transfer, two-song mashups, lyrics generation and editing, emotion-driven prompting, and music generation controls; MiniMax's music API closed to new users and the mmx CLI no longer provides a music command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luischarro](https://clawhub.ai/user/luischarro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and music creators use the skill's legacy MiniMax workflows to generate or transform music, create lyrics, and analyze audio. The release is deprecated; MiniMax music generation may no longer be available through its API or the mmx CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan assigns a suspicious verdict with medium confidence and notes privacy and scope concerns; some referenced material was only partially inspected.

Mitigation: Review the skill and its referenced material before use, and account for the scan's stated coverage limits.

Risk: Cloud workflows may send prompts, lyrics, reference audio, or cover and mashup inputs to MiniMax, which could expose private material.

Mitigation: Review cloud data handling and use only recordings, prompts, or lyrics you are comfortable sending to the service.

Risk: The skill is deprecated because MiniMax closed its music API to new users and the mmx CLI no longer includes a music command.

Mitigation: Confirm that the required MiniMax service and CLI functions remain available before relying on cloud-generation workflows; use the documented local music-craft alternative when they are unavailable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/luischarro/skills/music-craft-minimax)
- [Setup and preflight](references/setup-and-preflight.md)
- [MiniMax generation caveats](references/minimax-generation-caveats.md)
- [Cover workflow](references/cover-workflow.md)
- [Mashup workflow](references/mashup-workflow.md)
- [Audio analysis](references/advanced-audio-analysis.md)

## Skill Output:

**Output Type(s):** [Audio files, JSON analysis, Markdown guidance, Shell commands]

**Output Format:** [Audio files, JSON, and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio duration is approximate; local audio-analysis scripts can produce structured analysis even when cloud generation is unavailable.]

## Skill Version(s):

1.7.0 (source: artifact/SKILL.md frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
