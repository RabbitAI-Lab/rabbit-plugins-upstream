## Description: <br>
Use this skill when an AI agent needs to enrich a CSV lead list through the flashrev-ai-enrich npm CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flashlabs-ai](https://clawhub.ai/user/flashlabs-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to enrich lead-list CSV files through FlashRev, selecting live enrichment capabilities, validating mappings, previewing samples, and producing enriched CSV outputs with status, error, and spend reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lead enrichment can spend FlashRev tokens or contact credits, especially for contact unlocks and broad person enrichment. <br>
Mitigation: Check balance first, run dry-run and sample preview before live runs, and require explicit approval for spend, requested contact fields, and high-volume jobs. <br>
Risk: The customer_api capability can send row-derived data to a user-provided third-party endpoint. <br>
Mitigation: Confirm the destination domain before live runs, avoid mapping credentials or unrelated PII into headers or bodies, and prefer first-class FlashRev capabilities when available. <br>
Risk: Internal-target access can reach local, private, or metadata-network resources when deliberately enabled. <br>
Mitigation: Leave internal target blocking enabled by default and use --allow-internal-targets only after separate explicit approval in a trusted environment. <br>
Risk: Incorrect paths or overwrite choices can replace existing CSV outputs or enrich the wrong input file. <br>
Mitigation: Confirm source and output paths, inspect dry-run overwrite flags, and use --overwrite only after explicit approval. <br>
Risk: Capability names, inputs, or output fields may differ across connected FlashRev environments. <br>
Mitigation: Use only funcName values and field names returned by live schema --json, then validate mappings with dry-run before running enrichment. <br>


## Reference(s): <br>
- [FlashRev AI Enrich API Contract](references/api_contract.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/flashlabs-ai/skills/flashrev-ai-enrich) <br>
- [FlashRev Private App Settings](https://info.flashlabs.ai/settings/privateApps) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides agents to write enriched CSV files and report output paths, row status counts, row errors, and token or credit spend.] <br>

## Skill Version(s): <br>
1.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
