## Description:

Publishes existing static HTML files or site directories to GitHub Pages and returns a public URL, with a deploy.py helper for site, single-file, or enable-only workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gypalyson-creator](https://clawhub.ai/user/gypalyson-creator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and content creators use this skill to publish existing static web content to GitHub Pages when they need a shareable public URL and do not need backend services, databases, login, or private hosting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing to GitHub Pages can make static files publicly accessible.

Mitigation: Confirm the selected directory or file contains no secrets, private reports, customer data, or other sensitive content before deployment.

Risk: The deployment workflow requires GitHub write access and can affect repository contents.

Mitigation: Use a narrowly scoped fine-grained GitHub token limited to the target repository with Contents read/write permission, and revoke temporary tokens after use.

Risk: Security evidence notes that the skill overstates that it will never overwrite existing remote content.

Mitigation: Review the target repository, branch, and remote path before running uploads, especially when updating files that already exist.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/gypalyson-creator/github-pages-publish)
- [ClawHub skill page](https://clawhub.ai/gypalyson-creator/skills/github-pages-publish)
- [GitHub Pages API reference](references/pages-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and Python script usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces public GitHub Pages URLs and deployment instructions; the bundled script uses GitHub API calls when supplied with a token.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
