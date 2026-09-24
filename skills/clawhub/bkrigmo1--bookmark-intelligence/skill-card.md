## Description:

Automatically monitors X bookmarks, fetches linked articles, analyzes content with AI, and surfaces project-relevant insights through local files and notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bkrigmo1](https://clawhub.ai/user/bkrigmo1)

### License/Terms of Use:

Proprietary - Licensed per user

## Use Case:

Developers and power users use this skill to turn X bookmarks and linked articles into summaries, key concepts, actionable items, and project-specific implementation ideas. It can run on demand or as a background monitor with optional notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to paste X session cookies that can access their account.

Mitigation: Use a low-privilege account where possible, keep cookies local, rotate them regularly, and remove the generated .env file when uninstalling.

Risk: The security review reports unsafe shell command construction around cookies and remote URLs.

Mitigation: Review the scripts before execution, avoid sensitive networks, and do not run the skill with privileged operating-system or platform accounts.

Risk: Background daemon behavior can continuously fetch remote bookmark links.

Mitigation: Run on demand until reviewed, constrain the runtime environment, and monitor PM2 logs and network access if daemon mode is enabled.

Risk: Payment and crypto features are described by the security evidence as unfinished and not independently verified.

Mitigation: Validate payment configuration and licensing workflows separately before accepting real payments or using production wallet and payment credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bkrigmo1/skills/bookmark-intelligence)
- [README](artifact/README.md)
- [Skill documentation](artifact/SKILL.md)
- [Sample analysis output](artifact/examples/sample-analysis.json)
- [Sample notification output](artifact/examples/sample-notification.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON analysis files, and optional notification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analyzed bookmark records to local storage and send high-priority notification summaries when configured.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
