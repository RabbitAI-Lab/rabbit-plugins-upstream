## Description:

This skill supports Better Proposals requests involving reading, creating, and updating account data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Better Proposals account through OOMOL, including reading account settings and listing or retrieving brands, companies, currencies, proposals, quotes, and templates. For actions that may change state, users should confirm payloads and effects before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users toward unverified remote installer scripts for the oo CLI.

Mitigation: Do not let an agent run installer commands automatically; install the CLI only from a trusted source and prefer version pinning plus checksum or signature verification.

Risk: Write-capable Better Proposals connector actions can change account state when payloads are incorrect or unexpected.

Mitigation: Fetch the live action schema before building a payload and confirm the exact write payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-better-proposals)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Better Proposals Homepage](https://betterproposals.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fetching each action's live schema before constructing connector payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
