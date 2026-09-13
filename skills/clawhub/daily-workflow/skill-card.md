## Description:

Daily Workflow helps agents orient, checkpoint, wrap up, and hand off project work by writing compact, evidence-backed project memory notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, project maintainers, and agent operators use this skill to preserve resumable project state across work sessions. It records status, verification boundaries, blockers, risks, and exact next actions without replacing project governance or acceptance records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated project memory may include project context, commands, blockers, risks, and file paths that should not be shared broadly.

Mitigation: Review generated Docs/ files before sharing them and keep credentials, sensitive records, large logs, and confidential source excerpts out of handoff notes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/englandtong/skills/daily-workflow)
- [SKILL.md](artifact/SKILL.md)
- [Quickstart](artifact/QUICKSTART.md)
- [Security Guide](artifact/SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown files and concise chat summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project-local Docs/ notes only when persistence is authorized; avoids secrets and preserves existing governance records.]

## Skill Version(s):

4.1.0 (source: server release metadata, SKILL.md, SECURITY.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
