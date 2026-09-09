## Description:

Operates the `javdb` CLI to search JavDB App API records for movies, people, tags, rankings, and collections, and to manage accounts, configuration, downloads, and viewing marks only when explicitly authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run `javdb` for JavDB discovery, detail lookup, rankings, comments, magnets, and authenticated list or watch-state workflows while preserving explicit authorization boundaries for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated features may store JavDB credentials and tokens under ~/.javdb-cli.

Mitigation: Do not read or display credential files, prefer interactive login in a private terminal, and disclose command-line credential exposure before any password-based login command.

Risk: Updates, downloads, account changes, configuration writes, and watch-state marks can change local files, installed binaries, or remote account state.

Mitigation: Require explicit user authorization for each sensitive action and confirm target paths or state changes before execution.

Risk: Network, authentication, or API failures could be misrepresented as empty results.

Mitigation: Check command exit status and report actual stderr or service errors instead of changing data sources or fabricating empty output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/flanchanxwo/skills/javdb-cli)
- [Project Homepage](https://github.com/FlanChanXwO/javdb-cli)
- [Authentication and Accounts](references/auth.md)
- [Discovery Workflow](references/discover.md)
- [Installation and Version Checks](references/install.md)
- [State Changes](references/state.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with CLI command snippets and optional JSON or NDJSON command output summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sensitive credential and token values must not be echoed; state-changing, update, download, account, and configuration actions require explicit user authorization.]

## Skill Version(s):

0.7.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
