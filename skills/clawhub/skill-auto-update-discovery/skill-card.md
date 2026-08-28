## Description:

Engine auto-update & discovery skill OpenClaw: scan, evaluate, update, test, install, verify, rollback — dengan validation gate dan safety agar update tidak merusak workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to manage the OpenClaw skill lifecycle: discovering available skills and updates, evaluating compatibility and security, applying approved changes, testing results, and rolling back when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying skill updates or installing new skills can affect active workflows, especially when sources are untrusted.

Mitigation: Require confirmation before updates or installs, and run security, compatibility, and quality checks before applying changes.

Risk: Major updates, missing dependency tools, active-use updates, or failed backups can break skill loading or leave the workspace in an uncertain state.

Mitigation: Block partial installs, queue updates for skills that are in use, keep a backup before important changes, verify after installation, and roll back or escalate when verification fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-auto-update-discovery)
- [Publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with status reports, recommendations, and command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes validation, approval, verification, and rollback guidance for skill lifecycle changes.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
