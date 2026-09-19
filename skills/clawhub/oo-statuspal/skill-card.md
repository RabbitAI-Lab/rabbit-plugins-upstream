## Description:

StatusPal helps agents search and read StatusPal data through the OOMOL-connected oo CLI instead of calling the StatusPal API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to inspect StatusPal incidents, services, page status, and page summaries through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may execute remote installer scripts without independent verification.

Mitigation: Review setup commands before installation and prefer a verified, version-pinned, signed, or package-manager source for the oo CLI.

Risk: Connector actions depend on live schemas and authenticated OOMOL/StatusPal connection state.

Mitigation: Inspect the action schema before constructing payloads and only run setup or connection steps after a matching auth, scope, connection, or command-not-found failure.

## Reference(s):

- [StatusPal homepage](https://www.statuspal.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [StatusPal skill page](https://clawhub.ai/oomol/skills/oo-statuspal)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
