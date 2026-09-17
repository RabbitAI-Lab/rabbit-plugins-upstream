## Description:

DocRaptor guides agents to inspect the OOMOL DocRaptor connector schema, run supported DocRaptor actions, and create hosted PDF or Excel documents from HTML or public URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to work with DocRaptor through an OOMOL-connected account, especially to create hosted PDF or Excel documents from raw HTML or public URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote installer scripts that could be unsafe if run without verification.

Mitigation: Review setup steps before installing the oo CLI, prefer verified or package-manager installation paths, and avoid piping remote scripts directly into a shell.

Risk: Document creation changes DocRaptor state and raw HTML payloads can have unintended output or billing effects.

Mitigation: Confirm the exact document-creation payload and expected effect with the user before running write actions.

## Reference(s):

- [DocRaptor homepage](https://docraptor.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return DocRaptor document download URLs and execution metadata from connector responses.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
