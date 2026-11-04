## Description:

Multi-agent deep review for code PRs in any repo, orchestrating Copilot and parallel subagents for adversarial, operational, and reference-comparison review with scope-based escalation, stale-finding triage, and a hard iteration cap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review pull requests with multiple review perspectives, escalating from simple Copilot review to adversarial, operational, and reference-comparison analysis for higher-risk changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change GitHub pull-request state from a broad natural-language review trigger.

Mitigation: Use an explicit invocation such as /code-review and require confirmation before adding Copilot as a reviewer, posting GitHub comments, creating issues, or pushing changes.

Risk: Automated review findings can be stale or misleading after fixes are pushed.

Mitigation: Read the file at HEAD before acting on repeated findings and stop Copilot review after two rounds as directed by the artifact workflow.

## Reference(s):

- [Code Review Skill Page](https://clawhub.ai/conorbronsdon/skills/code-review)
- [README](artifact/README.md)
- [Subagent Prompt Templates](artifact/patterns/subagent-prompts.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown with inline shell commands and structured review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subagent reports are capped at about 500 words and Copilot review is capped at two rounds.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
