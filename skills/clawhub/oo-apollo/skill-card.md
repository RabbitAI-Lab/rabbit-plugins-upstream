## Description:

Apollo helps agents search and read Apollo data through an OOMOL-connected Apollo account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to search Apollo organizations and people, enrich records, and retrieve API usage through an OOMOL-connected Apollo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands for the oo CLI.

Mitigation: Review or replace the CLI setup path before installation; use a verified, pinned, official package or a manually reviewed installer instead of allowing an agent to run remote install commands automatically.

Risk: Apollo data is sent through OOMOL's connector service.

Mitigation: Use the skill only for Apollo data the user intends to process through OOMOL, and confirm account connection and scope expectations before running connector actions.

Risk: Connector payloads may be malformed if action schemas change.

Mitigation: Fetch the live action schema with the oo CLI before constructing each payload.

## Reference(s):

- [Apollo Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-apollo)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Apollo Connection](https://console.oomol.com/app-connections?provider=apollo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Apollo connector schemas before running actions; command results are returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
