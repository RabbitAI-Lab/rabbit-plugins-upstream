## Description: <br>
Fetches Solana transaction logs for provided addresses or programs, validates addresses before pulling, and can parse results with optional Anchor IDL decoding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lkkchen](https://clawhub.ai/user/lkkchen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and blockchain analysts use this skill to pull Solana transaction history for an address or program, parse logs, and locate generated output files for follow-up analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create a local project and install npm packages. <br>
Mitigation: Run it in a dedicated working directory and review package installation before letting the workflow proceed. <br>
Risk: The skill may store a Helius API key in a project .env file. <br>
Mitigation: Use a limited key, review .env before committing files, and avoid printing or sharing the key. <br>
Risk: Queried Solana addresses may be sent to Helius or public Solana RPC services. <br>
Mitigation: Use a trusted RPC provider and avoid querying addresses that should not be disclosed to third-party services. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lkkchen/skills/fetch-solana-logs) <br>
- [Reference](artifact/reference.md) <br>
- [Examples](artifact/examples.md) <br>
- [Chinese documentation](artifact/SKILL.zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated JSON or NDJSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates target_solana_addr.json, .env, and per-address files under output/<addr>/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
