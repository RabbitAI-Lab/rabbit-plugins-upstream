## Description:

Skill 管理器 helps WorkBuddy users manage the full skill lifecycle, including listing, viewing, creating, deleting, searching, auditing, packaging, and installing local and marketplace skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bettermen](https://clawhub.ai/user/bettermen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy users use this skill to inspect and administer installed skills, run health audits, review skill details, package skills, and operate a local dashboard for skill inventory and cleanup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local dashboard exposes sensitive skill-management and deletion APIs without adequate access controls.

Mitigation: Run the dashboard only on a trusted machine, bind it to 127.0.0.1, avoid exposing the port, and restrict CORS before use.

Risk: Cleanup and delete workflows can remove local skill files.

Mitigation: Review deletion targets carefully, require confirmation for destructive actions, and validate paths before using cleanup or delete features.

Risk: The security verdict is suspicious.

Mitigation: Install only if the publisher is trusted and local controls are in place.

## Reference(s):

- [ClawHub Skill Manager release page](https://clawhub.ai/bettermen/skills/skill-manager)
- [Python](https://python.org)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Chart.js distribution](https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown, structured tables, shell commands, JSON audit reports, and local dashboard API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local skill directories, produce audit summaries, export JSON data, and propose or execute cleanup actions after confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
