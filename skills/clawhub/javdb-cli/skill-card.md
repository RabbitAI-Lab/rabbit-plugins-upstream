## Description:

Enables agents to operate the `javdb` CLI for JavDB search, detail lookup, entity and list navigation, authenticated list access, and explicitly authorized account or watch-state changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they explicitly need an agent to operate the `javdb` binary for JavDB discovery workflows, authenticated account checks, media-asset previews, or user-approved state changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can contact JavDB services and use saved CLI authentication during approved workflows.

Mitigation: Install and use it only when JavDB CLI operation is intended; run authenticated checks or saved-account workflows only for explicit user requests.

Risk: Reverse image search can upload an approved JPEG, PNG, or WEBP image to the configured search service.

Mitigation: Explain the privacy impact and proceed with image search only after the user approves that workflow.

Risk: Some commands can write local preview assets, update or install the CLI binary, or change JavDB account state.

Mitigation: Require explicit user authorization for installation, updates, asset downloads, configuration writes, account changes, and watched or want marks.

Risk: Saved authentication files may contain usernames, passwords, or tokens.

Mitigation: Do not read, print, summarize, upload, or include authentication file contents in diagnostics or responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flanchanxwo/skills/javdb-cli)
- [Project homepage](https://github.com/FlanChanXwO/javdb-cli)
- [Authentication and account guidance](artifact/references/auth.md)
- [Discovery workflow guidance](artifact/references/discover.md)
- [Installation and version guidance](artifact/references/install.md)
- [State-change guidance](artifact/references/state.md)
- [Troubleshooting guidance](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON or NDJSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local preview asset file paths only when the user explicitly requests asset downloads.]

## Skill Version(s):

0.8.0 (source: evidence.json release.version and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
