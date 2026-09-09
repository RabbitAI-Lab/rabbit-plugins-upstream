## Description:

Helps agent users, skill authors, maintainers, and teams create practical workflows, checklists, analysis, code changes, and decision support for Gog-style Google Workspace and CLI productivity work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to turn Gog-style Google Workspace and CLI productivity needs into actionable workflows, templates, implementation support, and validation notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate too often for ordinary Google Workspace or CLI requests.

Mitigation: Narrow trigger terms or disable implicit invocation before deployment when broad activation would interrupt unrelated work.

Risk: Generated workflows, checklists, or code-change guidance may not fully match the user's local environment or success criteria.

Mitigation: Review the produced artifact against the stated success criteria and test code or shell commands locally before relying on them.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper)
- [Gog Demand Signal](https://clawhub.ai/skills/gog)
- [GitHub Demand Signal](https://clawhub.ai/skills/github)
- [SegmentFault JavaScript Signal](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript Signal](https://segmentfault.com/t/typescript)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional code blocks, checklists, and implementation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and follow-up work.]

## Skill Version(s):

0.20260908.51704 (source: server release evidence, created 2026-09-08T05:20:29Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
