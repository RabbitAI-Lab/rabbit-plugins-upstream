## Description:

Helps agent users, skill authors, maintainers, and teams plan, debug, harden, and adapt Agent Browser-style workflows with practical artifacts, checklists, analysis, code changes, and verification notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to turn Agent Browser-style workflow needs into concrete plans, templates, checklists, code changes, or decision support. It is intended for browser, headless automation, CLI, reliability, setup hardening, and adjacent workflow tasks where assumptions and validation steps should be explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording and implicit invocation can make the skill appear in unrelated browser, automation, CLI, or bug-fix conversations.

Mitigation: Confirm the task fits the Agent Browser-style workflow scope before using the skill, and narrow trigger text or invocation policy during maintenance.

Risk: Workflow, code, shell command, or configuration guidance may be incomplete or unsuitable for a user's environment.

Mitigation: Review generated artifacts before execution, check assumptions against the target environment, and validate results against the stated success criteria.

Risk: The Chinese localization may be less precise than the English source material.

Mitigation: Review localized wording before publication or use when Chinese-language instructions are important to the deployment.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-agent-browser-workflow-helper)
- [Agent Browser Demand Signal](https://clawhub.ai/skills/agent-browser-clawdbot)
- [Ask HN Agent Workflow Discussion](https://news.ycombinator.com/item?id=49653369)
- [JavaScript Demand Signal](https://segmentfault.com/t/javascript)
- [TypeScript Demand Signal](https://segmentfault.com/t/typescript)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with optional inline code blocks, shell commands, configuration snippets, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are tailored to the user's stated outcome and should include assumptions, limits, and validation steps when helpful.]

## Skill Version(s):

0.20260911.40430 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
