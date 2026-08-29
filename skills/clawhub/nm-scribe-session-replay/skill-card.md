## Description:

Converts a Claude Code session JSONL file into an animated GIF terminal replay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn selected Claude Code session history into animated terminal replay GIFs for pull requests, tutorials, demos, and visual evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session replays may expose private code, secrets, customer data, or internal discussion from Claude session history.

Mitigation: Use the skill only for explicit session replay requests, prefer a specific session path, limit turns and visible layers, and inspect or redact generated GIFs before sharing.

Risk: Broad triggers can make session replay behavior easier to invoke than intended.

Mitigation: Confirm the user wants a replay and the chosen session is appropriate before parsing or rendering shareable output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-session-replay)
- [ClawHub publisher profile](https://clawhub.ai/user/athola)
- [clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline commands, generated VHS tape path, and rendered GIF path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a temporary VHS tape file and an animated GIF through the configured scry:vhs-recording integration.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
