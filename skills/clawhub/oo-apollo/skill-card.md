## Description:

Apollo helps agents search, read, enrich, and inspect Apollo data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Apollo through an OOMOL-connected account for organization search, people search, enrichment, API usage checks, and setup recovery when authentication or connection failures occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands for the oo CLI.

Mitigation: Review and verify the OOMOL CLI distribution path before running remote installer commands; prefer a safer verified installation channel when available.

Risk: Apollo connector actions depend on account authentication, scopes, and OOMOL-connected credentials.

Mitigation: Run connection or authentication setup only after a command fails with the matching error, and confirm payloads before using any action marked write or destructive.

## Reference(s):

- [ClawHub Apollo skill page](https://clawhub.ai/oomol/skills/oo-apollo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Apollo connection setup](https://console.oomol.com/app-connections?provider=apollo)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Apollo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
