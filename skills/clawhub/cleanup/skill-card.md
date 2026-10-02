## Description:

Automates session wrap-up by reviewing work, preserving useful knowledge, updating checklists, and suggesting next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users invoke this skill at session end to review work, persist useful findings, update task records, and plan follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session content and artifacts may be preserved in a RAG store or local pending-import files, including sensitive information.

Mitigation: Review or disable session persistence before using the skill with secrets, customer data, proprietary code, or sensitive operational details.

Risk: End-of-session automation may change task and checklist state or inspect agent hook configuration.

Mitigation: Review the enabled cleanup steps and resulting changes before relying on their output.

## Reference(s):

- [ClawHub cleanup skill](https://clawhub.ai/drumrobot/skills/cleanup)
- [Cleanup run guide](artifact/run.md)
- [RAG storage guide](artifact/rag-store.md)
- [Cleanup configuration guide](artifact/config.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with optional shell commands and local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update task records, checklists, and stored session knowledge.]

## Skill Version(s):

0.8.0 (source: ClawHub release and CHANGELOG, 2026-09-30; bundled frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
