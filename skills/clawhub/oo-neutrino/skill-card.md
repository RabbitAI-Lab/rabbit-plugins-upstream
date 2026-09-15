## Description:

Runs Neutrino API lookups through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Neutrino API lookups through an OOMOL-connected account, including IP blocklist checks, IP information, domain lookup, email validation, and phone validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Install the oo CLI from a verified source or inspect and verify the installer before execution; do not run the installer automatically as part of routine Neutrino lookups.

Risk: Connector action payloads may be incorrect if they are built from stale assumptions.

Mitigation: Inspect the live connector schema for the target action before constructing and running the JSON payload.

Risk: Future Neutrino actions marked as write or destructive could change or remove data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Neutrino API homepage](https://www.neutrinoapi.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before running Neutrino actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
