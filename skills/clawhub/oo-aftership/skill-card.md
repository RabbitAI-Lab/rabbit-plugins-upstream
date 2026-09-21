## Description:

AfterShip (aftership.com). Use this skill for AfterShip requests that read, create, update, or delete tracking data through the OOMOL-connected AfterShip connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage AfterShip shipment tracking records from an agent through the oo CLI, including listing, retrieving, creating, updating, completing, retracking, and deleting trackings. It also supports courier listing and courier detection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path uses an unpinned remote installer script executed by the shell.

Mitigation: Review the installer before running it, prefer an official package or version-pinned installer, and verify checksums or signatures where available.

Risk: AfterShip write and destructive actions can modify or delete shipment tracking records.

Mitigation: Confirm the exact action, target tracking record, payload, and expected effect with the user before approving state-changing commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aftership)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [AfterShip homepage](https://www.aftership.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
