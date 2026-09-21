## Description:

KoboToolbox helps agents operate KoboToolbox through an OOMOL-connected account for reading, creating, updating, deploying, exporting, validating, and deleting survey projects, library assets, and submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage KoboToolbox projects, library assets, submissions, validation state, and exports through the OOMOL `oo` CLI connector. It supports read-only, write, and destructive workflows with confirmation expectations for actions that change or remove data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can execute a remote installer script for the oo CLI.

Mitigation: Review the oo CLI installation path before installation and prefer a verified or package-manager install when available.

Risk: Write and destructive actions can create, deploy, validate, export, overwrite, or delete KoboToolbox data.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running any write or destructive action.

## Reference(s):

- [KoboToolbox homepage](https://www.kobotoolbox.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kobotoolbox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses `oo connector schema` before constructing payloads and `oo connector run --json` for KoboToolbox actions.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
