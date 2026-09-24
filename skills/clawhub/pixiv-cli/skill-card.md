## Description:

Operate Pixiv through the installed pixiv CLI for discovery, reverse image search, account actions, and downloads with explicit authorization and credential safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent operate pixiv-cli for Pixiv searches, reverse image lookup, account-scoped reads, bookmarks, follows, comments, and downloads while preserving explicit consent boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through credential import, export, backup, restore, and account selection workflows.

Mitigation: Require explicit user authorization for each credential action, keep refresh tokens and export bundles out of commentary and logs, and use private output paths or direct consumer pipelines except for explicitly confirmed stdout disclosure.

Risk: Bookmark, follow, comment, download, configuration, update, and MCP server actions can change account state, local files, or long-lived processes.

Mitigation: Confirm the exact current target, scope, destination, and state change before each invocation; do not carry authorization forward to later commands.

Risk: Reverse image search may upload a local image or URL to third-party providers such as SauceNAO or ascii2d.

Mitigation: Use only images or URLs the user is authorized to share, preserve provider privacy boundaries, and avoid echoing API keys, source URLs, temporary paths, or upstream response bodies in diagnostics.

Risk: Paged searches, local filters, bookmark-count strategies, and multi-provider reverse search can produce partial or bounded results.

Mitigation: Report limits, pagination, filter completeness, and partial provider failures accurately; do not claim a bounded result set is exhaustive unless the requested traversal completed.

## Reference(s):

- [pixiv-cli homepage](https://github.com/FlanChanXwO/pixiv-cli)
- [Pixiv CLI ClawHub page](https://clawhub.ai/flanchanxwo/skills/pixiv-cli)
- [CLI reference drawing-tool catalog](https://github.com/FlanChanXwO/pixiv-cli/blob/main/docs/en/cli-reference.md#drawing-tool-catalog)
- [Authentication import and export](references/auth.md)
- [Discovery playbooks](references/discover.md)
- [Download workflows](references/download.md)
- [Explicit installation workflow](references/install.md)
- [Troubleshooting decision tree](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and summaries of Pixiv CLI text, JSON, or NDJSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads write files locally after explicit target and destination confirmation; account and credential actions require explicit user authorization.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
