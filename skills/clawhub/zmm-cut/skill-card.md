## Description:

詹明明·口播剪辑 guides an agent through a personalized ChatCut workflow for turning recorded talking-head footage into a publishable Douyin edit with speech cleanup, pacing, captions, and delivery checkpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Creators or operators editing the 詹明明 account's talking-head videos use this skill to keep ChatCut edits aligned with fixed account defaults and step-by-step review checkpoints. It is suited for a single-person workflow that preserves the spoken script while cleaning fillers, pauses, repetitions, pacing, and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads configured vault reference files and writes persistent editing lessons under the zmm-cut memory folder.

Mitigation: Review the configured vault and memory paths before use if local editing preferences or account-specific notes should not be retained.

Risk: The workflow depends on ChatCut and scoped local reference files being available.

Mitigation: Confirm ChatCut access and required reference files before starting an editing session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-cut)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown instructions with tool-use checkpoints and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow guidance for ChatCut editing; final media export is only requested when the user explicitly asks for export or download.]

## Skill Version(s):

0.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
