## Description:

Scan markdown files and verify that all hyperlinks, both local files and remote URLs, resolve correctly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to audit Markdown files before publishing, release, archiving, or static-site generation by identifying broken local and remote hyperlinks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker makes network requests to remote links found in selected Markdown files, which can disclose private or sensitive URLs to those remote hosts.

Mitigation: Run it only on documentation directories intended for audit, and review or remove sensitive URLs before checking remote links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/markdown-link-check)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and plaintext link-check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports broken links with file paths, line numbers, diagnostic reasons, and process exit codes.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
