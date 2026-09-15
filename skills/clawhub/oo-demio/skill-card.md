## Description:

Demio enables agents to use the OOMOL-connected oo CLI to read Demio events and sessions, list participants, and register attendees after user confirmation for write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Demio through an OOMOL-connected account, including retrieving event and session data, listing participants, and registering attendees. It is intended for Demio workflows where agents should inspect live connector schemas and ask for confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review the official install guide, verify installer integrity where possible, and avoid blindly running remote installer pipelines.

Risk: The register_attendee action changes Demio state and returns attendee-specific join information.

Mitigation: Inspect the live action schema and get user confirmation for the exact payload and effect before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-demio)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Demio Homepage](https://www.demio.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent outputs may include oo CLI connector schema commands, connector run commands, requested confirmation text for write actions, and summarized connector results.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
