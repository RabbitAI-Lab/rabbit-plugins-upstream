## Description:

Aircall (aircall.io) supports Aircall requests that search, list, and read calls, contacts, numbers, teams, and users through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Aircall connector schemas and run read-only Aircall retrieval and listing actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run an unverified remote installer script in a shell.

Mitigation: Install the oo CLI from a verified, versioned source, inspect installer contents first, and avoid elevated privileges.

Risk: Normal connector use sends Aircall call, contact, number, team, and user data through OOMOL.

Mitigation: Use an approved OOMOL-connected Aircall account and request only the data needed for the task.

## Reference(s):

- [ClawHub Aircall Skill](https://clawhub.ai/oomol/skills/oo-aircall)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Aircall](https://aircall.io)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
