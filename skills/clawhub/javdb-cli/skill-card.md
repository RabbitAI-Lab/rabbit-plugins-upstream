## Description:

JavDB CLI helps agents operate the `javdb` binary to search JavDB App API content, inspect details, comments and magnets, and perform explicitly authorized account, configuration, download and viewing-state actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to operate the JavDB CLI for JavDB-specific search, entity navigation, magnet lookup, account diagnostics, and clearly authorized state or configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates an adult-content JavDB account workflow and may cause local credential storage or network API requests.

Mitigation: Use it only for explicit JavDB tasks, require confirmation before login or account operations, and never read, print or summarize stored credentials or tokens.

Risk: State changes, downloads, auto-relogin, proxy or host changes, updates and image reverse search can affect local files, account state, traffic routing or privacy.

Mitigation: Confirm the exact target and action before each operation, require new output paths for downloads, disclose image upload implications, and avoid persistent configuration changes without clear user approval.

Risk: Authentication, network, parameter or service errors could be mistaken for empty results.

Mitigation: Check command exit status, report the actual failure reason, and do not silently switch data sources, accounts, hosts, proxies, retries or scraping strategies.

## Reference(s):

- [javdb-cli homepage](https://github.com/FlanChanXwO/javdb-cli)
- [Authentication and Account Guidance](references/auth.md)
- [Search and Navigation Workflows](references/discover.md)
- [Installation and Version Checks](references/install.md)
- [State Changes](references/state.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON or NDJSON handling notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct use of structured javdb output; credential, state-changing, download, proxy, host and image-upload actions require explicit user authorization.]

## Skill Version(s):

0.7.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
