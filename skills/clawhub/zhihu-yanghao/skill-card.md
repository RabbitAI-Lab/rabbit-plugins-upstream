## Description:

This skill guides an agent through a configurable Zhihu account-nurturing workflow using ego-browser, including topic selection, answer drafting and publishing, moment posting, engagement actions, and verification steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to run a configurable Zhihu growth routine for an authenticated account, including scheduled answer publishing, moment posting, topic rotation, and controlled engagement actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, like, follow, collect, comment, and edit content from an authenticated Zhihu account.

Mitigation: Review generated content, configuration, and action parameters before execution, prefer dry-run paths where available, and use only an account whose public activity risk is acceptable.

Risk: The workflow asks users to disable sandbox protections for ego-browser commands.

Mitigation: Disable sandbox protections only when the operational need and added risk are understood, then re-enable them after the task.

Risk: Automated posting or engagement patterns may trigger Zhihu account limits or platform enforcement.

Mitigation: Follow the documented pacing limits, keep one answer per shift at most, space engagement actions, and reduce to one answer per day if the account is limited.

Risk: Configuration and /tmp parameter files control live account actions.

Mitigation: Keep configuration and parameter files under the user's control, avoid sharing them, and remove transient files when they are no longer needed.

## Reference(s):

- [Risk control reference](references/risk-control.md)
- [Selectors reference](references/selectors.md)
- [Topic strategy reference](references/topic-strategy.md)
- [Workflow reference](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, and JavaScript automation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can lead to live public Zhihu account actions when the user executes scripts in an authenticated ego-browser session.]

## Skill Version(s):

1.3.1 (source: server release metadata, SKILL.md heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
