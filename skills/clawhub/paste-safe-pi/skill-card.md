## Description:

Emit shell commands that survive being pasted into a remote terminal that garbles non-ASCII input and mangles multi-line or long pastes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sharinchan233](https://clawhub.ai/user/sharinchan233)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they need paste-safe shell guidance for remote terminals, especially Raspberry Pi or SSH sessions where non-ASCII text, long commands, or multi-line blocks are corrupted during manual paste.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated sed or echo commands may modify files on the target machine if pasted without review.

Mitigation: Review each command before pasting and use the paired read-back command to confirm the intended change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sharinchan233/skills/paste-safe-pi)
- [Publisher profile](https://clawhub.ai/user/sharinchan233)
- [paste-safe-pi worked examples](artifact/reference.md)

## Skill Output:

**Output Type(s):** [shell commands, markdown, guidance]

**Output Format:** [Markdown with short single-line shell commands and read-back checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended to be pure ASCII and usually under 90 characters per line.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
