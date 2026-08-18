## Description:

Helps AI-agent users and skill authors plan, harden, debug, and adapt Gog-style Google Workspace workflows into concrete checklists, artifacts, analyses, or implementation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External AI-agent users, skill authors, maintainers, and teams use this skill to turn Gog-style Google Workspace workflow needs into practical plans, checklists, implementation support, and validation notes. It is most useful when a request involves debugging, setup hardening, reliability improvement, or an adjacent workflow inspired by the same job-to-be-done.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate too broadly for unrelated Google, CLI, or bug-fix tasks because its trigger wording is generic and implicit invocation is enabled.

Mitigation: Explicitly name the intended skill for unrelated work and review this skill's proposed workflow before applying it.

Risk: Generated workflow, code, shell command, or configuration guidance may not match the user's exact Google Workspace environment or permissions.

Mitigation: Validate assumptions, credentials, permissions, and any generated commands or code against the user's local setup before applying changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper)
- [Gog ClawHub Demand Signal](https://clawhub.ai/skills/gog)
- [GitHub ClawHub Demand Signal](https://clawhub.ai/skills/github)
- [Hacker News Demand Signal](https://news.ycombinator.com/item?id=49338865)
- [V2EX Workflow Safety Signal](https://www.v2ex.com/t/1235217)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional inline code blocks, checklists, and validation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include assumptions, constraints, remaining risks, and follow-up work.]

## Skill Version(s):

0.20260818.40417 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
