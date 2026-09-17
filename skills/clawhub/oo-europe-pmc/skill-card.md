## Description:

Europe PMC lets an agent search and retrieve Europe PMC literature, preprints, annotations, citations, references, grants, full-text XML, evaluations, status checks, and associated data links through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and research-support agents use this skill to search Europe PMC and retrieve publication records, annotations, citations, references, full-text XML, grants, evaluations, data links, and article or preprint status through OOMOL connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of remote installer scripts for the oo CLI.

Mitigation: Prefer a verified installer or package-manager path, review installer contents when available, and avoid elevated shells.

Risk: Connector payloads may include unpublished research, credentials, or sensitive personal data.

Mitigation: Do not send sensitive data unless OOMOL's handling is acceptable for the use case.

## Reference(s):

- [ClawHub Europe PMC skill page](https://clawhub.ai/oomol/skills/oo-europe-pmc)
- [Europe PMC homepage](https://europepmc.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON from oo connector actions when run with --json.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
