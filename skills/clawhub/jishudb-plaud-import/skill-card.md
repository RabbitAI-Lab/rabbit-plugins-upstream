## Description:

Archives selected Plaud recordings, audio, transcripts, and summaries in JishuDB, preserving source associations and supporting cited meeting comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Users with authorized Plaud recordings or local exports use this skill to archive selected meeting audio and text in JishuDB, preserve their associations, and optionally compare meetings against cited project documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings and transcripts may contain sensitive meeting information transferred to JishuDB.

Mitigation: Confirm the selected material, destination, and write authorization before transfer; do not expose credentials or signed URLs in the report.

Risk: Optional desktop installation and client configuration can affect the local environment and account permissions.

Mitigation: Require explicit approval and review installer source, hashes, destination paths, client changes, OAuth/write scope, and any unsigned Windows publisher prompt.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/jishudb-plaud-import)
- [Declared skill homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-plaud-import)
- [Plaud MCP documentation](https://docs.plaud.ai/plaud-mcp-cli/mcp)
- [Connection and transfer guidance](references/connection-and-transfer.md)
- [JishuDB setup guidance](references/jishudb-setup/setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown status report with saved IDs and citations when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports material coverage, processing status, and any recovery action.]

## Skill Version(s):

0.1.5 (source: server-resolved release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
