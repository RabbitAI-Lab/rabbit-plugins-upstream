## Description:

Files.com (files.com). Use this skill for Files.com requests that read, create, update, or delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Files.com through the oo CLI, including listing folders, retrieving metadata, downloading files, creating folders, deleting paths, and updating custom metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote pipe-to-shell installer commands, and the security scan flagged this as needing human review before use.

Mitigation: Use a verified installer or inspect and validate the downloaded installer script before running it; do not let the agent run pipe-to-shell installation automatically.

Risk: The skill can create folders, update metadata, and delete Files.com paths.

Mitigation: Confirm the exact Files.com action, target path, payload, and expected effect before approving write or destructive operations.

## Reference(s):

- [Files.com homepage](https://www.files.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-files-com)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce downloaded file references from connector transit storage when the download_file action is used.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
