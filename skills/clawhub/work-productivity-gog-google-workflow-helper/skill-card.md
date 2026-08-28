## Description:

Helps agent users and skill maintainers turn Gog-style Google Workspace workflow demand into practical plans, checklists, analyses, code changes, and verification notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to adapt popular Gog-style Google workflow patterns into reliable local-hardware-friendly plans, templates, scripts, checklists, analyses, and implementation support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit trigger wording may activate the skill for general Google, Gmail, Drive, Calendar, CLI, or bug-fix requests.

Mitigation: Narrow the trigger language or disable implicit invocation when precise routing is needed.

Risk: Workflow outputs may include plans, scripts, or code changes that affect workspace setup, safety, or reliability.

Mitigation: Review generated artifacts against user constraints and run normal tests or scans before deployment.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper)
- [Popular ClawHub Skill Demand: Gog](https://clawhub.ai/skills/gog)
- [Popular ClawHub Skill Demand: GitHub](https://clawhub.ai/skills/github)
- [Tell HN: Gmail can mark legitimate google.com mail as spam](https://news.ycombinator.com/item?id=49465624)
- [SegmentFault JavaScript Topic](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript Topic](https://segmentfault.com/t/typescript)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are tailored to the user's immediate workflow and should expose assumptions, limits, required inputs, and any remaining risks.]

## Skill Version(s):

0.20260828.40337 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
