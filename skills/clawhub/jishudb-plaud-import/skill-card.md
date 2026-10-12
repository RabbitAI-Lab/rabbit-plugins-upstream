## Description:

Archives selected Plaud recordings, audio, timestamped transcripts, and meeting summaries in JishuDB from an authorized connector or local export, preserving source associations for later comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams archive selected Plaud meetings in a JishuDB knowledge base, preserve links between their audio and text, and optionally compare them with cited project documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional JishuDB Desktop installation changes the local environment.

Mitigation: Review and approve the release, digest, install location, endpoint port, and client entry before setup.

Risk: Importing meeting recordings or transcripts can transfer sensitive material to the wrong knowledge base.

Mitigation: Confirm the selected Plaud material, destination knowledge base, and write permission before import.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bowen-aijishu/skills/jishudb-plaud-import)
- [Project homepage (listed in release metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-plaud-import)
- [Plaud MCP documentation](https://docs.plaud.ai/plaud-mcp-cli/mcp)
- [Plaud CLI documentation](https://docs.plaud.ai/plaud-mcp-cli/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown status report and optional cited comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports saved material, provenance, processing status, and any recovery action.]

## Skill Version(s):

0.1.8 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
