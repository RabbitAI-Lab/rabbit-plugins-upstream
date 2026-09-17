## Description:

Skill Audit & Publish guides agents through auditing, sanitizing, verifying, publishing, and install-checking OpenClaw skills for ClawHub releases, with optional GitHub synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to prepare OpenClaw skills for ClawHub publication by staging a publish folder, auditing for private data or credentials, checking metadata and versioning, requiring approval, and verifying installation after publish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing can expose skill contents publicly and may be difficult to undo cleanly.

Mitigation: Review the exact file list, target slug, version, destination, and sanitized content before approving any publish action.

Risk: Credentials could be exposed if tokens are passed or stored carelessly.

Mitigation: Use narrowly scoped GitHub tokens through environment variables only, and avoid command-line token arguments or token files.

Risk: Using a mutable one-shot ClawHub CLI runner can introduce supply-chain risk.

Mitigation: Use a pinned or locally installed ClawHub CLI version where possible before running publish or install-check commands.

Risk: The optional GitHub sync helper only creates or updates files, so removed local files can remain in the remote repository.

Mitigation: Audit the remote repository file list after major restructures and remove stale files manually when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [Publish Rules for ClawHub & GitHub](artifact/references/publish-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, file manifests, rewritten skill files, audit checklists, and optional JavaScript sync commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates local publish folders and approval messages; optional GitHub sync helper creates or updates files only and does not delete remote files.]

## Skill Version(s):

1.5.7 (source: evidence.json release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
