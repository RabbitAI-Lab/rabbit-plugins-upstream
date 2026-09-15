## Description:

CaptainBI helps agents query CaptainBI business, sales, inventory, store, refund, and return data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected CaptainBI account use this skill to fetch live connector schemas and run CaptainBI reporting and lookup actions for Amazon business operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run installer commands automatically; install the oo CLI only after user approval from a trusted, pinned release with checksum or signature verification where available.

Risk: Authentication, CaptainBI connection, and billing recovery steps affect the user's OOMOL account.

Mitigation: Require the user to approve login, connection, and billing actions directly before proceeding.

Risk: CaptainBI action payloads can be incorrect if the agent assumes stale input schemas.

Mitigation: Fetch the live action schema before constructing each JSON payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-captainbi)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [CaptainBI Homepage](https://www.captainbi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated OOMOL oo CLI connection; action payloads should be built after fetching the live connector schema.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
