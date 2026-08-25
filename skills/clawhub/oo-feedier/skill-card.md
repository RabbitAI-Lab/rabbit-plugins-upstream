## Description:

Feedier enables agents to list, retrieve, create, update, delete, and share Feedier analytical reports through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Feedier reports from an agent session, including report lookup, creation, updates, deletion, and expiring share-link generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Feedier reports.

Mitigation: Review the exact connector payload and intended effect before approving create_report, update_report, or create_report_share_link.

Risk: The destructive action can delete a Feedier report.

Mitigation: Confirm the target report ID and require explicit approval before delete_report runs.

Risk: First-time setup can install the oo CLI and connect a Feedier account through OOMOL.

Mitigation: Install and connect only when the user intends the agent to operate that Feedier account.

## Reference(s):

- [ClawHub Feedier skill](https://clawhub.ai/oomol/skills/oo-feedier)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Feedier homepage](https://www.feedier.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.0 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
