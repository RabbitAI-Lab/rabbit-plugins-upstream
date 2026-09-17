## Description:

Streamtime integration that lets an agent read, create, and update Streamtime data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected Streamtime account use this skill to inspect action schemas and run Streamtime connector actions for organisation, company, contact, job, branch, rate-card, and user workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts.

Mitigation: Review the install path before use and prefer an official signed or checksum-verified oo CLI installer, or download and inspect the installer before executing it.

Risk: Write actions can create or update Streamtime business records.

Mitigation: Confirm the exact payload and expected effect with the user before allowing create or update actions.

Risk: The connected Streamtime account determines what data and operations the skill can access.

Mitigation: Only connect the Streamtime account intended for OOMOL operation and confirm account scope before running actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-streamtime)
- [Streamtime Homepage](https://www.streamtime.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
