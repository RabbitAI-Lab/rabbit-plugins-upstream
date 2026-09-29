## Description:

Browser automation skill for setting up a bsession environment, fetching information from websites, creating one-shot or recurring browser automations, and debugging existing sessions from any repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gaxxx](https://clawhub.ai/user/gaxxx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to operate browser sessions in a Docker-backed bsession environment, extract website information, create reusable browser scripts, and troubleshoot browser automation sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can execute unverified remote code when a custom repository or installer source is used.

Mitigation: Only install from trusted sources, prefer a pinned reviewed repository, and inspect setup inputs before running installation.

Risk: The skill builds and runs Docker content and can persist browser automation state on the host.

Mitigation: Review Docker Compose behavior before starting containers, use --no-start during review, and monitor writes under ~/.bsession, ~/.claude, and ~/.openclaw.

Risk: Passing sensitive VNC passwords on the command line can expose credentials through shell history or process listings.

Mitigation: Avoid command-line secrets and configure sensitive values through a safer local secret handling process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gaxxx/skills/bsession)
- [ClawHub publisher profile](https://clawhub.ai/user/gaxxx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, generated Python automation scripts, and configuration file guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker and may create or modify persistent bsession workspace files under the user's home directory.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
