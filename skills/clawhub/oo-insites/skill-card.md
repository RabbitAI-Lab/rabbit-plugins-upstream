## Description:

Insites (insites.com). Use this skill for any Insites request, including reading, creating, updating, and auditing data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Insites audits from an OOMOL-connected account. It supports reading audit status and reports, searching audits, and starting SEO and AEO website audits after confirming state-changing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the installation path, prefer a signed or package-manager installation, avoid elevated execution, and verify downloaded content before running it.

Risk: Starting an Insites audit changes account state.

Mitigation: Confirm the exact connector action payload and expected effect with the user before running any write action.

Risk: Connector schemas may change over time.

Mitigation: Fetch the live action schema with oo connector schema before constructing or submitting a payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-insites)
- [Insites Homepage](https://insites.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Insites Icon](https://static.oomol.com/logo/third-party/insites.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, connector schema inspection steps, connector run payloads, audit identifiers, and report retrieval guidance.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
