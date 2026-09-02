## Description:

Presents adaptive codebase challenge questions with multiple-choice and trace exercises.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and contributors use this skill to answer adaptive questions about a codebase and receive scored feedback that can update Gauntlet progress state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and updates local .gauntlet challenge state and developer progress.

Mitigation: Use it in repositories where Gauntlet state tracking is intended, and review .gauntlet changes when state updates matter.

Risk: If a pending challenge exists, the skill may treat the latest user message as the challenge answer.

Mitigation: Confirm or clear pending challenge state before invoking the skill when the latest message should not be scored.

## Reference(s):

- [Gauntlet homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet)
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-challenge)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown and local Gauntlet state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and update local .gauntlet challenge state and developer progress.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
