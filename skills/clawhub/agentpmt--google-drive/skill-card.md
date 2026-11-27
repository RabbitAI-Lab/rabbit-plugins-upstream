## Description:

Search, organize, upload, download, share, and export Google Drive files through AgentPMT-hosted tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can manage Google Drive files and folders, including searching, transfers to and from AgentPMT storage, organization, sharing, and export of Google Workspace documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected account and shared-drive access may expose files or incur usage charges.

Mitigation: Connect only an account whose files the agent should manage, and check shared-drive access and usage charges.

Risk: Permanent deletion and public sharing can have consequential effects.

Mitigation: Explicitly authorize permanent deletion and public sharing before those actions are taken.

Risk: Downloaded content passes through AgentPMT storage, and setup instructions or unpinned installs may change.

Mitigation: Review setup skills and updates before enabling them, and verify installation sources rather than relying on unpinned commands.

## Reference(s):

- [AgentPMT Google Drive marketplace page](https://www.agentpmt.com/marketplace/google-drive)
- [ClawHub skill release](https://clawhub.ai/agentpmt/skills/google-drive)

## Skill Output:

**Output Type(s):** [Files, File metadata, Text]

**Output Format:** [Google Drive file results and content, including exported Google Workspace documents.]

**Output Parameters:** [Action-dependent; may include file IDs, search queries, folder paths, export formats, and sharing permissions.]

**Other Properties Related to Output:** [Downloaded content passes through AgentPMT storage.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
