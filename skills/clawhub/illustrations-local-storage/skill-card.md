## Description:

Localize HTTP(S) images in SoMark Markdown into ZIP-like directory packages for one Markdown file or a batch of .md/.markdown files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[soul-code](https://clawhub.ai/user/soul-code)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to persist remote SoMark Markdown images locally, rewrite image links to relative paths, and package one document or a batch of Markdown files for offline or durable use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads remote images referenced by Markdown and writes local output files.

Mitigation: Process untrusted Markdown with --allowed-host for known storage domains and review the generated package before using it downstream.

Risk: Installing the Pillow dependency with pip changes the active Python environment.

Mitigation: Install only in an environment where running pip is acceptable, such as an isolated virtual environment.

Risk: Using --force can replace existing output files.

Mitigation: Use --force only when overwriting existing Markdown packages or images is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/soul-code/skills/illustrations-local-storage)
- [Publisher profile](https://clawhub.ai/user/soul-code)

## Skill Output:

**Output Type(s):** [markdown, files, shell commands, guidance]

**Output Format:** [Markdown packages with local image files and concise execution guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each processed document produces main.md and an images/ directory; batch runs produce one isolated package per source document.]

## Skill Version(s):

0.1.0 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
