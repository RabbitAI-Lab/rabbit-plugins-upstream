## Description:

Extracts a user's writing voice from text samples via SICO comparative analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

External users and writing-focused agent operators use this skill to collect writing samples, compare them against baseline model output, and create local voice profiles and registers for consistent generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores writing samples and generated voice profiles locally, and those materials may contain sensitive personal or business information.

Mitigation: Use only samples the user is comfortable storing under ~/.claude/voice-profiles, confirm consent for any third-party text, and delete samples or profiles after use when retention is not needed.

Risk: Weak anonymization or retention practices can leave identifying context in saved samples and profile artifacts.

Mitigation: Strip filenames, dates, URLs, and proper nouns before extraction; review manifest and profile files for residual identifiers before reuse or sharing.

Risk: Detector-related wording and project-level .voice/override.md files may steer later writing workflows in unintended ways.

Mitigation: Review generated craft rules, banned phrases, and any project override files before applying the profile in downstream generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-extract)
- [clawdis homepage: claude-night-market scribe](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration]

**Output Format:** [Markdown guidance with local profile files, JSON manifests, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates extraction.md, manifest.json, and register markdown files under ~/.claude/voice-profiles/{name}.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
