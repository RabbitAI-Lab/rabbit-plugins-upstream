## Description:

This skill guides an agent through a configurable Zhihu account-nurturing workflow that can publish answers and moments, run engagement actions, verify posted content, and apply topic, pacing, and content-quality guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

External users and agent operators use this skill to run a Zhihu growth routine for a logged-in account, including topic selection, answer drafting, posting, lightweight engagement, and post-publication verification. It is intended for users who accept the account and platform-policy risks of automating public activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, edit, like, follow, collect, or comment through a logged-in Zhihu account.

Mitigation: Use it only with an account intended for this automation, keep manual review or dry-run modes enabled where available, and confirm content before public posting.

Risk: The skill asks users to disable sandbox protections for ego-browser operations.

Mitigation: Run it on an isolated machine or account and re-enable sandbox protections after the task.

Risk: Shared /tmp parameter files can affect live posting workflows.

Mitigation: Avoid shared /tmp files for real posting unless file ownership checks and explicit confirmation are added.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/zhihu-yanghao)
- [Risk Control](references/risk-control.md)
- [Workflow](references/workflow.md)
- [Topic Strategy](references/topic-strategy.md)
- [Selectors](references/selectors.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON, JavaScript, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce public Zhihu content drafts and account-operation commands that should be reviewed before execution.]

## Skill Version(s):

1.3.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
