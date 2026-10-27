## Description:

Archive Zoom cloud recordings, read stored meeting transcripts and summaries, or manage a Zoom meeting through zm. Use for Zoom CLI workflows, not joining calls or operating the desktop video client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Zoom account owners and their agents use the CLI to find and review archived meeting evidence, archive cloud recordings, prepare for meetings, and perform explicitly authorized meeting changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting transcripts and summaries can contain sensitive information, and remote embedding services may receive transcript passages beyond local search filters.

Mitigation: Select only the intended Zoom profile and communications accounts or folders; use local models or avoid embedding when remote disclosure is not acceptable.

Risk: MCP changes can execute without another prompt, and meeting creation, updates, or cancellations affect remote accounts.

Mitigation: Authorize changes explicitly, review previews and targets, and restart MCP after changing or revoking source access.

Risk: Saved recording archives and indexes may retain sensitive meeting data after source access changes.

Mitigation: Manage archive and index retention separately from Zoom profile and communications access.

## Reference(s):

- [Zoom CLI on ClawHub](https://clawhub.ai/wirecat/skills/zoom-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples and JSON output selectors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command-specific bounds and evidence references may be included in results.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
