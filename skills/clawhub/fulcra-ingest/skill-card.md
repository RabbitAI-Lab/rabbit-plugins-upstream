## Description:

Autonomously orchestrate the ingestion of 3rd-party data exports (e.g., Spotify, Netflix) from the Fulcra File Store into properly mapped Fulcra Annotations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fulcra](https://clawhub.ai/user/fulcra)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to ingest user-provided third-party exports into Fulcra Annotations, including schema profiling, idempotent record creation, source mapping, archival, and ingest logging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated fetching or polling can collect sensitive third-party exports without enough user awareness.

Mitigation: Confirm the data source, collection frequency, destination, privacy implications, and stop procedure before enabling automation.

Risk: Enrichment, deletion, or reprocessing workflows can expose or mutate personal data.

Mitigation: Require explicit user confirmation before enrichment, record deletion, schema changes, or re-ingestion workflows.

Risk: Moving ingested files by download, upload, and delete can cause data loss if archival is incomplete.

Mitigation: Verify the archived file exists with Fulcra file listing or stat commands before deleting the original ingest file.

Risk: Concurrent source-map updates can overwrite lineage or archive metadata from another run.

Mitigation: Download the latest source map before updating it and perform a version or freshness check before upload.

## Reference(s):

- [Fulcra CLI for 3rd-Party Data Ingestion](references/fulcra-ingest-cli.md)
- [Fulcra Ingest Source Mapping](references/fulcra-ingest-source-mapping.md)
- [Fulcra CLI documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-get-started/references/fulcra-cli.md)
- [Fulcra timeline](https://context.fulcradynamics.com/timeline?mode=week&date=YYYY-MM-DD)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python snippets, and JSONL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Fulcra CLI commands, local parsing scripts, ingestion logs, source-map updates, deterministic UUIDs, and concise status summaries.]

## Skill Version(s):

0.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
