## Description:

Signaturely (signaturely.com). Use this skill for Signaturely folder requests, including reading, creating, and updating folder data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Signaturely action schemas and manage Signaturely folders from an OOMOL-connected account. It supports listing and retrieving folders, plus confirmed state-changing folder creation and renaming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a remote installer command for the oo CLI.

Mitigation: Review the installer source before use and prefer an official, reviewable, version-pinned installation path when available.

Risk: The allowed oo CLI permission is broader than the listed Signaturely folder actions.

Mitigation: Install and run the skill only in an environment where broader OOMOL CLI access is acceptable, and confirm write-action payloads before execution.

## Reference(s):

- [ClawHub Signaturely Skill](https://clawhub.ai/oomol/skills/oo-signaturely)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Signaturely Homepage](https://signaturely.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, an authenticated OOMOL account, and a connected Signaturely provider before live connector actions can run.]

## Skill Version(s):

1.0.2 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
