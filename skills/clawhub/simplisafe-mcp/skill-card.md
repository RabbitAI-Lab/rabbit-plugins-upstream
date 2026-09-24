## Description:

Query and control a SimpliSafe alarm system from the shell with curl, including system state, sensors, locks, events, settings, and arm, disarm, lock, or unlock actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable users use this skill to inspect and operate their own SimpliSafe system from an agent-assisted shell workflow, including authenticated status checks, event review, and explicit arm, disarm, lock, or unlock commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control high-impact SimpliSafe alarm and lock actions, including arm, disarm, lock, unlock, and PIN-reading commands.

Mitigation: Require explicit user confirmation outside the helper before any arm, disarm, lock, unlock, or PIN-reading command.

Risk: The security evidence reports weak executable safeguards and an unsafe token cache path.

Mitigation: Install only where authenticated SimpliSafe control is acceptable, prefer a single-user machine, and use a private TMPDIR or fix token cache handling before operation.

## Reference(s):

- [SimpliSafe curl + jq recipes](artifact/references/recipes.md)
- [SimpliSafe shell helpers](artifact/references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated API calls and explicit confirmation guidance for physical security actions.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
