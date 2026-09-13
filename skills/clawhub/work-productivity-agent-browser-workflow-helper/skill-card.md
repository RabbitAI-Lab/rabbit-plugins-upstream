## Description:

Helps agent users, skill authors, maintainers, and teams create practical workflows, checklists, analysis, code changes, and decision support for Agent Browser-style productivity automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, agent users, skill authors, maintainers, and teams use this skill to turn Agent Browser-style productivity needs into local-friendly workflows, implementation plans, checklists, analysis, code changes, or decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked by broad browser, automation, or productivity prompts.

Mitigation: Review or narrow trigger metadata before deployment when precise activation is required.

Risk: Workflow or code-change proposals can be incorrect or unsuitable for a user's environment.

Mitigation: Review generated artifacts against the stated success criteria and test code or shell commands before applying them.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [Work Productivity Agent Browser Workflow Helper on ClawHub](https://clawhub.ai/kyro-ma/skills/work-productivity-agent-browser-workflow-helper)
- [Popular ClawHub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot)
- [Ask HN: Those running agents 24/7, what's your workflow and what are they doing?](https://news.ycombinator.com/item?id=49653369)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, code snippets, shell commands, and configuration snippets depending on the user's request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and follow-up work when useful.]

## Skill Version(s):

0.20260911.40430 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
