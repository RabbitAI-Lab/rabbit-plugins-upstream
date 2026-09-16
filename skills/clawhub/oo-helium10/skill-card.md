## Description:

Helium 10 connector skill that lets agents search and read Helium 10 data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover available Helium 10 tools and run approved read-only Helium 10 actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a remote pipe-to-shell installer for the oo CLI.

Mitigation: Use a pinned and verifiable oo CLI installation path, review the installer before execution, and avoid running remote installer commands blindly.

Risk: Helium 10 requests and account-derived business data are routed through OOMOL.

Mitigation: Install only when OOMOL is an acceptable processor for the user's Helium 10 data, and confirm before transmitting confidential business or account-derived data.

## Reference(s):

- [Helium 10 homepage](https://www.helium10.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-helium10)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Helium 10 connector result JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
