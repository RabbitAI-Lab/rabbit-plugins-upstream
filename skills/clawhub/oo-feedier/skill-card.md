## Description:

Operate Feedier through an OOMOL-connected account to read, create, update, delete, and share analytical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Feedier analytical reports through the OOMOL connector, including report creation, listing, retrieval, updates, deletion, and share-link generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Feedier reports and can generate report share links.

Mitigation: Confirm the exact action, payload, target report, and intended effect with the user before running write actions.

Risk: The delete_report action removes a Feedier report.

Mitigation: Require explicit user approval for the report ID or target before running destructive actions.

Risk: Share-link creation may expose access to Feedier analytical reports.

Mitigation: Create share links only for report targets the user recognizes and approves.

## Reference(s):

- [Feedier homepage](https://www.feedier.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Feedier skill page](https://clawhub.ai/oomol/skills/oo-feedier)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live Feedier connector schema inspection before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
