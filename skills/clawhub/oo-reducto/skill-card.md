## Description:

Reducto helps agents operate Reducto through an OOMOL-connected account to extract structured data, parse documents, and split documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access Reducto document-processing actions through the OOMOL oo CLI. It supports schema inspection, structured data extraction, document parsing, and document splitting for Reducto-supported documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can ask an agent to run remote installer scripts for the oo CLI.

Mitigation: Review the installer command before execution and prefer independently verified official instructions or a signed/package-managed release.

Risk: Connector actions depend on the user's OOMOL account connection, credentials, scopes, and billing state.

Mitigation: Run setup or reconnection steps only after an authentication, connection, scope, or billing error and confirm account state before retrying.

## Reference(s):

- [Reducto homepage](https://reducto.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include a data object and meta.executionId when connector actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
