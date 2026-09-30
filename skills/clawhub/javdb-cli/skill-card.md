## Description:

Operate the installed javdb CLI to search the JavDB App API, inspect movie and entity references, read lists, and perform explicitly authorized account, configuration, mark, or preview-asset actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to operate an installed javdb CLI for scoped JavDB discovery, authenticated list access, explicit account or configuration changes, marks, preview-asset handling, and installation/update checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an installed javdb CLI to make JavDB account, configuration, mark, cache, file download, or update changes.

Mitigation: Require an explicit current target and action before performing state-changing, file-writing, or update operations.

Risk: Authentication data may include local usernames, passwords, and JWTs.

Mitigation: Do not read, print, upload, quote, or summarize local credential files; use private interactive login flows when credentials are needed.

Risk: Image search uploads selected images to AVScan or another configured reverse-search provider.

Mitigation: Explain the upload privacy effect and use image search only with an authorized source.

Risk: Preview asset operations can download files or expose incomplete media outcomes.

Mitigation: Confirm the requested asset scope and destination, preserve errors, and report only verified download results.

## Reference(s):

- [JavDB CLI homepage](https://github.com/FlanChanXwO/javdb-cli)
- [ClawHub skill page](https://clawhub.ai/flanchanxwo/skills/javdb-cli)
- [Authentication and Accounts](references/auth.md)
- [Discovery and Navigation](references/discover.md)
- [Installation and Updates](references/install.md)
- [Preview Media Assets](references/media.md)
- [Explicit State Changes](references/state.md)
- [Errors, Network, and Routing](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and summarized CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON or NDJSON excerpts when explicitly requested and safe to disclose.]

## Skill Version(s):

0.8.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
