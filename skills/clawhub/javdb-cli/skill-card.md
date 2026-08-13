## Description:

Safely operates the javdb-cli `javdb` binary to search JavDB content, inspect details, retrieve magnets, and manage authenticated account, configuration, and watch-state actions when explicitly authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent translate explicit JavDB-related requests into checked `javdb` CLI workflows for discovery, authenticated lists, magnet lookup, troubleshooting, and authorized state changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored JavDB credentials, passwords, or JWTs could be exposed through auth files, logs, command arguments, or agent responses.

Mitigation: Do not read or echo `~/.javdb-cli/auth.json`; prefer interactive login, warn before command-line credential use, and never repeat passwords or tokens.

Risk: The skill can trigger local or remote state changes, including account selection, configuration writes, media downloads, software updates, and watch markers.

Mitigation: Require explicit authorization for each state-changing action and confirm the target, action, and output path before running the command.

Risk: The skill may contact JavDB APIs, retrieve magnet information, or route traffic through configured hosts and proxies.

Mitigation: Use it only for explicit JavDB-related tasks, report command errors as-is, and do not change host, proxy, account, retry, or scraping behavior without user direction.

## Reference(s):

- [javdb-cli homepage](https://github.com/FlanChanXwO/javdb-cli)
- [ClawHub skill page](https://clawhub.ai/flanchanxwo/skills/javdb-cli)
- [Authentication and accounts](references/auth.md)
- [Discovery and navigation workflows](references/discover.md)
- [Installation and version checks](references/install.md)
- [State changes requiring explicit authorization](references/state.md)
- [Errors, network, and proxy handling](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and JSON-output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user authorization before credentials, account state, local files, software updates, or remote watch-state changes.]

## Skill Version(s):

0.5.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
