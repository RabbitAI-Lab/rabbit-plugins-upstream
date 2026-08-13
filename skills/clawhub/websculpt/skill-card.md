## Description:

WebSculpt bootstraps browser automation and command-library skills for agents that need to gather external information, scrape pages, call APIs, or repair an unavailable WebSculpt setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bqw1013](https://clawhub.ai/user/bqw1013)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to install, verify, update, or route WebSculpt browser automation workflows. It is aimed at users who need repeatable access to external web information, including content-wall workflows, scraping, API access, and command-library maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install global npm packages and persistent agent lifecycle skills under the user's home directory.

Mitigation: Review the install scope before use; prefer project-local installation when WebSculpt is needed for only one workspace.

Risk: Future agent sessions may automatically use installed WebSculpt lifecycle skills after setup.

Mitigation: Proceed only if persistent WebSculpt lifecycle behavior is acceptable for the environment.

Risk: The scanner summary notes broad triggers without a clear consent checkpoint.

Mitigation: Confirm user intent before installation, update, repair, or persistent skill changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bqw1013/skills/websculpt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install or route persistent lifecycle skills and global CLI tooling when the WebSculpt environment is missing or broken.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
