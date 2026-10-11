## Description:

Archives selected Plaud recordings, audio, transcripts, and meeting summaries in JishuDB, preserving source associations for verified retrieval and optional cited comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

People archiving selected Plaud meetings or authorized local exports use this skill to save audio and text in JishuDB, preserve their source associations, and optionally compare them with cited project documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: JishuDB Desktop installation or client configuration changes may affect the user's environment.

Mitigation: Review the proposed release, destination paths, permissions, and client changes; approve the concrete setup plan before execution.

Risk: Selected recordings and transcripts may contain sensitive meeting information.

Mitigation: Authorize the Plaud/JishuDB connections and confirm the selected material and destination before uploading; decline if a local-only export is required.

## Reference(s):

- [Project page listed in skill metadata (not verified import provenance)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-plaud-import)
- [Plaud MCP documentation](https://docs.plaud.ai/plaud-mcp-cli/mcp)
- [Plaud CLI documentation](https://docs.plaud.ai/plaud-mcp-cli/cli)
- [Connection and transfer guide](artifact/references/connection-and-transfer.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports saved IDs, material coverage, processing status, and cited comparisons when requested.]

## Skill Version(s):

0.1.7 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
