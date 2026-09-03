## Description:

Improves a voice profile by learning from manual edits to refine registers and close voice drift over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers use this skill after manually editing generated text to compare post-review and final drafts, identify recurring voice patterns, and propose updates to voice profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores generated drafts, reviewed drafts, and final manual edits as local voice-profile snapshots.

Mitigation: Use it only when the local profile storage and any sync behavior are acceptable for the writing being processed; avoid confidential writing unless that storage has been reviewed.

Risk: Learning proposals can introduce incorrect or unwanted voice rules into the profile.

Mitigation: Review the evidence and proposed profile changes before approving any update.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-learn)
- [Scribe plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown proposals and summaries, JSON accumulator entries, and local profile file updates when approved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses three-stage snapshot comparison and requires user approval before applying proposed profile changes.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
