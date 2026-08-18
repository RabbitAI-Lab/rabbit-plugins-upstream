## Description:

GitHub Desktop Chinese localization tool that detects installed loose or asar-packaged GitHub Desktop resources, applies dictionary-based JavaScript string replacements, and supports preview, deployment, rollback, and syntax validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent preview, apply, or roll back Chinese localization changes for a local GitHub Desktop installation. It is intended for workflows where modifying installed application resources is acceptable and recoverable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify installed GitHub Desktop application files.

Mitigation: Use --dry-run first, close GitHub Desktop before deployment, and keep backups enabled so rollback remains available.

Risk: Broad trigger phrases may cause an agent to start a patching workflow without enough user confirmation.

Mitigation: Require explicit user intent before deployment and prefer preview or analysis responses until the user confirms a write action.

Risk: Using --force or --no-backup reduces recovery protection.

Mitigation: Avoid --force and --no-backup unless the user understands the recovery tradeoff and has another way to restore GitHub Desktop.

Risk: Asar or Node tooling on PATH participates in extraction, repacking, or syntax validation.

Mitigation: Use only trusted asar and node binaries from the user's expected environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/github-desktop-zh)
- [Server-resolved GitHub repository](https://github.com/ebandao777-oss/github-desktop-zh)
- [Server-resolved GitHub commit](https://github.com/ebandao777-oss/github-desktop-zh/tree/ba16e730ea176d9d73e8081d46b021bcdf82ca4c)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide preview, deployment, rollback, and validation of local changes to GitHub Desktop application files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports tool version 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
