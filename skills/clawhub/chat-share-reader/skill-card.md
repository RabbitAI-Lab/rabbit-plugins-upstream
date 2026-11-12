## Description:

Export, back up, or archive AI chat conversations to markdown from public share links and local agent session stores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mapleleo-hub](https://clawhub.ai/user/mapleleo-hub)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users can convert public AI conversation links and locally stored agent sessions into searchable Markdown archives, then export selected conversations for backup or context reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan inspected only 5 of 35 components and its tool-misuse analysis was degraded, so its review is incomplete.

Mitigation: Seek a more complete scan and review the package execution path before deciding whether to install.

Risk: ClawScan reports concerns involving package execution, browser endpoints, and archive handling.

Mitigation: Review these areas in the artifact and consider ClawScan's recommendation not to install before deciding.

## Reference(s):

- [Chat Share Reader on ClawHub](https://clawhub.ai/mapleleo-hub/skills/chat-share-reader)
- [Local session formats](references/sessions.md)
- [Supported share sites](references/sites.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Text]

**Output Format:** [Markdown conversation archives, optional JSON, or text printed to standard output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can export one or more conversations and filter local session searches by keyword or working directory.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
