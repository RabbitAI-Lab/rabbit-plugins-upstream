## Description: <br>
Use the local kalshi CLI for bounded Kalshi series and market research, keyword discovery, portfolio and candlestick reads, order reconciliation, and explicitly confirmed demo or production order operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bobashopcashier](https://clawhub.ai/user/bobashopcashier) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to guide bounded Kalshi CLI research, portfolio inspection, order reconciliation, and carefully controlled demo or production order operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Kalshi credentials or private keys could be exposed if placed in command arguments, params, logs, or prompts. <br>
Mitigation: Use the configured credentials file or API key and private key file environment variables, keep credential files at mode 0600 or stricter, and avoid placing private keys in generated commands or output. <br>
Risk: Live order actions can mutate demo or production accounts if executed without review. <br>
Mitigation: Prefer demo mode, require an explicit environment and write policy, run dry-run first, review the canonical plan, then repeat the identical command with the confirmation digest only after approval. <br>
Risk: Schema drift, truncation, or pagination can cause incomplete or incorrect market and portfolio interpretation. <br>
Mitigation: Parse stable contract fields, require needed fields, set bounded page/item/byte limits, inspect truncation and continuation metadata, and treat upstream schema mismatches as contract failures. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented output instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers compact JSON, bounded pagination and byte limits, stable error codes, and explicit dry-run confirmation for writes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
