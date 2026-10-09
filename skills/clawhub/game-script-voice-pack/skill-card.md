## Description:

Turns attributed game or murder-mystery scripts into ordered, labeled multi-character voice clips with consistent voices per role.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers, interactive storytellers, and tabletop creators use this skill to cast script characters and produce ordered, importable dialogue clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device token grants broad account access across installed Beatra skills.

Mitigation: Install only where shared Beatra account permissions are acceptable and keep the device token private.

Risk: The package silently updates its own files by default.

Mitigation: Review the update policy before installing; disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if undesired.

Risk: Voice synthesis and optional cloning spend credits, and cloning a voice without permission can misuse a person's identity.

Mitigation: Confirm the cast and live cost estimate before paid calls; clone a voice only after the speaker's authorization is confirmed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/game-script-voice-pack)
- [Game voice-pack workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Audio files, Markdown, Text]

**Output Format:** [Numbered voice clips with a cast sheet and line-by-line delivery details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Clips retain script order and character and line IDs; delivery includes duration, MIME type, audio location, model, and actual credits charged when available.]

## Skill Version(s):

0.1.6 (source: server-resolved release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
