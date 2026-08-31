## Description:

This skill guides an agent through a configurable Zhihu account-nurturing workflow using ego-browser, including topic rotation, answer drafting and publishing, engagement actions, moments posting, and publication checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Account operators and developers use this skill to run a configurable Zhihu growth routine for a logged-in account, including topic selection, answer creation, engagement actions, and risk controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a logged-in Zhihu account and may publish, like, follow, collect, or comment without a final human approval step.

Mitigation: Require manual review before any account action is sent, use dry-run modes where available, and keep optional comment, follow, and collection actions disabled unless intentionally needed.

Risk: The skill requires weakened sandboxing to run ego-browser commands.

Mitigation: Use a dedicated browser profile or account on a machine without sensitive data, keep secrets out of config and temp files where possible, and re-enable sandboxing after the task.

Risk: High-frequency account activity can trigger platform rate limits or account restrictions.

Mitigation: Honor the documented timing intervals, keep each session to at most one answer or one moment, and reduce the schedule to one answer per day if the account is limited.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/zhihu-yanghao)
- [Risk control guidance](artifact/references/risk-control.md)
- [Workflow and script usage](artifact/references/workflow.md)
- [Topic strategy](artifact/references/topic-strategy.md)
- [DOM selectors and ego-browser API notes](artifact/references/selectors.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JavaScript automation scripts, shell command examples, and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces account-action guidance and executable browser-automation scripts that should be reviewed before use on a logged-in Zhihu account.]

## Skill Version(s):

1.3.0 (source: server release metadata and artifact title)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
