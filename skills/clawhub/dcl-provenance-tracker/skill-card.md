## Description: <br>
DCL Provenance Tracker compares trusted baseline and candidate ClawHub skill versions to identify version drift, permission creep, and supply chain attack patterns, then returns a deterministic DCL provenance proof. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill after ClawHub skill updates or in CI/CD gates to compare two supplied skill versions locally and decide whether an update should pass, warn, or block. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow asks users to paste both skill versions into the agent context for local comparison. <br>
Mitigation: Run the comparison in an approved agent environment and avoid pasting sensitive or proprietary skill content into unapproved contexts. <br>
Risk: The optional DCL Trust Oracle MCP lookup is separate from local diffing and may involve paid tx_hash verification. <br>
Mitigation: Configure or use the MCP server only when the separate record verification step is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daririnch/skills/dcl-provenance-tracker) <br>
- [DCL Trust Oracle MCP server](https://mcp.fronesislabs.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes verdict, risk score, version hashes, DCL fingerprint, findings, categories checked, recommendation, and timestamp.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
