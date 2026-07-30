## Description: <br>
DCL Semantic Drift Guard checks an LLM response against a provided source or configured knowledge-base query to identify hallucinations, contradictions, omissions, and fabricated specifics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to verify that generated summaries, answers, or decisions remain grounded in an authoritative source before delivery or commit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using kb_query or the optional MCP pre-check can send user-provided text or queries outside the agent context. <br>
Mitigation: Use the default context mode for confidential or sensitive material, and enable network modes only after confirming external transmission is acceptable. <br>
Risk: The optional MCP pre-check records audit metadata on-chain. <br>
Mitigation: Use the optional pre-check only when recording audit metadata is acceptable; otherwise rely on the local verification workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daririnch/skills/dcl-semantic-drift-guard) <br>
- [DCL Trust Oracle MCP endpoint](https://mcp.fronesislabs.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [JSON verdict with confidence, drift items, source mode, strictness, audit hash, and timestamp.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default context mode is local-only; kb_query and the optional MCP pre-check are network-enabled modes that require user confirmation for sensitive material.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
