## Description:

Archive selected Plaud audio, transcripts, or summaries in JishuDB; preserve provenance and verify imports before cited follow-up analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to archive selected Plaud recordings, transcripts, or summaries into a chosen JishuDB knowledge base while preserving source associations. It supports resumed imports, verification of saved material, and optional cited comparison against existing knowledge-base evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could import the wrong recording, representation, or destination knowledge base if the user selection is ambiguous.

Mitigation: Require explicit approval of the selected source material, transfer route, and destination KB before reading or writing.

Risk: Plaud credentials, token files, signed download URLs, upload headers, or sensitive account and device identifiers could be exposed during transfer.

Mitigation: Use authorized connectors, keep temporary URLs and upload credentials out of persisted provenance and reports, and avoid reading token files or printing sensitive identifiers.

Risk: Audio archival can be incomplete when direct upload, decoder, speech, size, duration, or host byte-transfer capability is unavailable.

Mitigation: Check live JishuDB audio capabilities before upload, preserve observed partial state, and report a concrete recovery action instead of silently substituting transcript-only import.

Risk: Interrupted or repeated runs could duplicate material or lose source association history.

Mitigation: Use stable recording identities, reconcile existing documents and provenance notes before writing, and append changed content as revisions rather than overwriting prior records.

Risk: Follow-up analysis could overstate evidence when imported material has not been read back or indexed.

Mitigation: Verify saved documents with readback and retrieval checks before offering cited analysis, and label incomplete processing as PARTIAL.

## Reference(s):

- [Connection and Transfer](references/connection-and-transfer.md)
- [Recording Provenance Record](references/provenance-record.md)
- [Plaud MCP documentation](https://docs.plaud.ai/plaud-mcp-cli/mcp)
- [Plaud CLI documentation](https://docs.plaud.ai/plaud-mcp-cli/cli)
- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/jishudb-plaud-import)
- [OpenClaw homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-plaud-import)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown status reports with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports completion state, saved identifiers, material coverage, processing status, readback status, and recovery actions while excluding credentials, signed URLs, upload headers, and sensitive account or device identifiers.]

## Skill Version(s):

0.1.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
