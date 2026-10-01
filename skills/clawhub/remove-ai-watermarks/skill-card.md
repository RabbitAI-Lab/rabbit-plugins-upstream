## Description:

Guides agents to identify and remove AI watermarks and provenance marks from images and video that users own or are allowed to edit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can inspect AI provenance signals and remove selected labels or metadata from their own images and video. The skill does not cover watermarks protecting third-party paid assets.

### Deployment Geography for Use:

Global, subject to local restrictions on AI-label removal

## Known Risks and Mitigations:

Risk: Media files can be altered or overwritten during removal.

Mitigation: Work only on files the user is allowed to edit and use a separate output path rather than overwriting the source.

Risk: Installation may add Python packages to the local environment.

Mitigation: Review the required dependencies and obtain user approval before installing them.

Risk: Removing a local provenance signal could be mistaken for proof that content is human-made or safe to misrepresent.

Mitigation: Report only observed results and never treat removal or a negative check as proof of origin or permission to misrepresent it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project repository (listed in skill metadata)](https://github.com/wiltodelta/remove-ai-watermarks)
- [Project homepage](https://raiw.cc)
- [Command recipes](references/commands.md)
- [Installation and optional dependencies](references/install.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed results and output paths; absence of a local signal does not establish human authorship.]

## Skill Version(s):

1.0.10 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
