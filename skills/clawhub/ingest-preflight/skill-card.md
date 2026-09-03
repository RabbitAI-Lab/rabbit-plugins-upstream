## Description:

Before publishing to ClawHub, validate a skill-shaped folder (required files, frontmatter, size, auth, slug availability, and a dry-run publish) with one script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill publishers use this skill to run a repeatable preflight check on a packaged ClawHub skill folder before publishing. It helps catch missing required files, incomplete frontmatter, oversized files, missing authentication, slug conflicts, and dry-run publish failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke an authenticated ClawHub CLI and run a dry-run publish for the folder supplied by the user.

Mitigation: Run it only against packaged skill folders intended for publication, and confirm the folder path and active ClawHub identity before execution.

## Reference(s):

- [DESCRIPTION.md](references/DESCRIPTION.md)
- [Ingest Preflight on ClawHub](https://clawhub.ai/terrycarter1985/skills/ingest-preflight)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with bash command examples and terminal status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a target skill folder path and optional slug; returns pass, warning, or failure feedback from preflight checks.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
