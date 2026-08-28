## Description:

Runs parallel prose and craft review agents against a voice profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and content teams use this skill to review generated or existing prose against a voice profile, separate hard failures from advisory craft feedback, and apply accepted edits before saving the final text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-provided text and voice register content during review.

Mitigation: Use it only with text and profile material you are comfortable sharing with the active agent workflow.

Risk: Hard-failure fixes are applied automatically before advisory decisions.

Mitigation: Review the diff after hard fixes and before accepting or saving the final text.

Risk: Learning mode can save local snapshots of reviewed text.

Mitigation: Enable learning mode only for content that is acceptable to store in local voice-profile snapshots.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-review)
- [Scribe plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown advisory tables plus edited text and status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the final reviewed text and, when learning mode is enabled, local post-review and post-fix snapshots.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
