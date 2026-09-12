## Description:

Operate Pixiv through the pixiv-cli binary to search illustrations, novels, and users; reverse-search images; inspect Pixiv works and profiles; view rankings and recommendations; manage bookmarks and follows; and download works.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to operate Pixiv through the pixiv-cli command line tool for discovery, account-aware reads, account mutations, reverse-image search, downloads, and troubleshooting. The skill is intended for explicit Pixiv or pixiv-cli tasks and tells the agent to verify installed command syntax before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install workflow can run a mutable remote installer and may replace a local binary or change PATH.

Mitigation: Review the install workflow before use, prefer a pinned or independently verified installer when possible, and require the installer to report SHA-256 verification before replacement.

Risk: Credential import and export workflows can expose Pixiv refresh tokens or plaintext authentication bundles.

Mitigation: Run credential transfer only for an explicit user request, avoid stdout secret disclosure unless explicitly confirmed, and do not log, parse, summarize, or repeat secret material.

Risk: Bookmark, follow, download, FANBOX, reverse-image upload, and MCP startup actions can affect accounts, write files, share image data with providers, or start long-lived processes.

Mitigation: Use those actions only when explicitly intended, confirm target IDs and destinations before execution, and verify that any image or URL sent to SauceNAO or ascii2d is authorized for upload.

## Reference(s):

- [pixiv-cli repository](https://github.com/FlanChanXwO/pixiv-cli)
- [Authentication import and export](references/auth.md)
- [Discovery playbooks](references/discover.md)
- [Download workflows](references/download.md)
- [Explicit installation workflow](references/install.md)
- [Troubleshooting decision tree](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or NDJSON command output when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output should reduce result volume at the source, avoid exposing credentials, confirm state-changing or disk-writing actions, and inspect exit status before parsing structured output.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
