## Description:

Operate ngrok through an OOMOL-connected account by inspecting connector schemas and running read-oriented ngrok actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect ngrok endpoint, reserved domain, tunnel session, and tunnel data through an OOMOL-managed connector without handling raw ngrok credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote installer directly in a shell.

Mitigation: Prefer a verified or package-manager installation of the oo CLI, and avoid running the remote installer from an elevated shell.

Risk: The skill depends on OOMOL as an intermediary for access to the user's ngrok account.

Mitigation: Install only if the user trusts OOMOL for this account connection, and use the skill for intended ngrok account resource reads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ngrok)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ngrok homepage](https://ngrok.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON from the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
