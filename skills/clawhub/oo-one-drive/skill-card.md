## Description:

Use this skill for OneDrive requests that read, create, update, or delete data through the OOMOL one_drive connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate OneDrive through an OOMOL-connected account, including file and folder reads, metadata lookup, search, uploads, folder creation, content replacement, metadata updates, and recycle-bin deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run unverified installer scripts from the internet.

Mitigation: Review the setup path before installing, use the skill only if OOMOL and the oo CLI installation source are trusted, and prefer a verified or package-manager installation.

Risk: Upload, update, and delete actions can change OneDrive data.

Mitigation: Confirm the exact target, payload, and expected effect before running write actions, and treat delete_item as destructive even though it moves items to the recycle bin.

## Reference(s):

- [ClawHub OneDrive skill page](https://clawhub.ai/oomol/skills/oo-one-drive)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Microsoft OneDrive](https://www.microsoft.com/microsoft-365/onedrive/online-cloud-storage)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector JSON responses when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
