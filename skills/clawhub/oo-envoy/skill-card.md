## Description:

Envoy (envoy.com). Use this skill for Envoy requests that search and read data through the OOMOL Envoy connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and employees use this skill to read Envoy employees, sign-in flows, invites, and locations through an OOMOL-connected account. It supports fetching individual records and listing records with optional filters and pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes running a remote oo CLI installer directly in a shell without verification.

Mitigation: Review the installer source and prefer a verified or official installation path with checksums or signatures before installing.

Risk: Connecting Envoy exposes selected Envoy data through the OOMOL connector.

Mitigation: Connect only Envoy scopes the user is comfortable exposing and keep usage focused on the listed read-only get and list actions.

## Reference(s):

- [Envoy homepage](https://envoy.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; read actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
