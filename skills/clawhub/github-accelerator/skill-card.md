## Description:

Use when GitHub access fails: fallback mirrors for git.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youbuwei](https://clawhub.ai/user/youbuwei)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agents use this skill to keep public GitHub clone and file-download workflows moving when direct GitHub access is slow or unavailable. It provides probe-first guidance, fallback mirror commands, and local private proxy configuration patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clone cleanup behavior can delete an existing folder if the destination path already exists.

Mitigation: Never pass an existing directory as the clone destination, and fix the clone cleanup behavior before routine use.

Risk: Third-party mirrors or public proxies can expose repository URLs or sensitive download links.

Mitigation: Use the skill only for public GitHub resources or trusted private proxy infrastructure, and avoid signed or credential-bearing URLs.

Risk: The skill includes guidance for authenticated repository writes through GitHub APIs.

Mitigation: Require explicit user confirmation before any API-based commit or ref update.

Risk: Persistent proxy configuration changes can alter future network routing for GitHub downloads or clones.

Mitigation: Require explicit confirmation before writing proxy configuration, and keep local proxy files out of published artifacts.

## Reference(s):

- [GitHub Accelerator on ClawHub](https://clawhub.ai/youbuwei/skills/github-accelerator)
- [README](README.md)
- [Skill Definition](SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local proxy configuration and GitHub download or clone commands; command results should be verified by the agent or user.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
