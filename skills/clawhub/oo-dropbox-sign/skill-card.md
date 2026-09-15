## Description:

Dropbox Sign (sign.dropbox.com). Use this skill for Dropbox Sign requests involving searching and reading account, signature request, and template data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Dropbox Sign through an OOMOL-connected account, retrieving account properties, signature requests, and templates through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Install the oo CLI only from a trusted and reviewed distribution path, and avoid pipe-to-shell installation unless the installer source has been verified.

Risk: The routing language is broader than the listed read-only Dropbox Sign actions.

Mitigation: Use the skill for the documented get, list, and search actions unless a separate review approves state-changing Dropbox Sign operations.

Risk: Connector operations depend on an OOMOL-connected Dropbox Sign account and server-side credential handling.

Mitigation: Confirm the intended OOMOL account connection and inspect the live connector schema before sending payloads.

## Reference(s):

- [Dropbox Sign homepage](https://sign.dropbox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Dropbox Sign skill page](https://clawhub.ai/oomol/skills/oo-dropbox-sign)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI commands, connector schema inspection steps, JSON payload examples, and summarized Dropbox Sign read results.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
