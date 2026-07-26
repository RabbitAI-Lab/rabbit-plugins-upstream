## Description: <br>
Autonomously orchestrate the ingestion of 3rd-party data exports from the Fulcra File Store into properly mapped Fulcra Annotations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to ingest personal third-party export data, map it to Fulcra Annotations, archive processed files, and keep ingestion lineage records up to date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated fetching could collect data from external APIs, local services, or CLI tools without the user's intended cadence or scope. <br>
Mitigation: Require explicit confirmation of the source, frequency, destination, privacy implications, and stop instructions before enabling automation. <br>
Risk: Archive cleanup and record correction workflows can delete files or previously ingested Fulcra records. <br>
Mitigation: Confirm destructive actions before running delete commands, and verify archive upload destinations before removing original files. <br>
Risk: Incorrect schema or source mapping can create duplicate or misclassified Fulcra Annotations. <br>
Mitigation: Use the source map and catalog checks before schema creation, record deterministic ID fields, and update ingestion lineage after processing. <br>


## Reference(s): <br>
- [Fulcra Ingest CLI Reference](references/fulcra-ingest-cli.md) <br>
- [Fulcra Ingest Source Mapping](references/fulcra-ingest-source-mapping.md) <br>
- [Fulcra Ingest on ClawHub](https://clawhub.ai/fulcra/skills/fulcra-ingest) <br>
- [Fulcra CLI Documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-onboarding/references/fulcra-cli.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSONL examples, and generated parsing or ingestion code when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local ingestion scripts, source-map updates, ingest logs, and deterministic record identifiers during an authorized workflow.] <br>

## Skill Version(s): <br>
0.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
