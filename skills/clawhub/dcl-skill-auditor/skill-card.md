## Description: <br>
DCL Skill Auditor helps agents perform pre-install static security reviews of ClawHub skills and return structured PASS, WARN, or BLOCK audit results, with an optional paid DCL Trust Oracle MCP check. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent operators, and marketplace reviewers use this skill before installing or updating ClawHub skills to identify credential theft, prompt injection, data exfiltration, suspicious shell or network activity, and permission abuse patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional DCL Trust Oracle check uses a paid external network call and wallet/payment flow. <br>
Mitigation: Use the offline checklist for local-only review unless the organization accepts the external call, payment flow, and data handling policy. <br>
Risk: Static checklist results can miss issues outside the covered attack patterns or create false confidence if used as the only review gate. <br>
Mitigation: Treat PASS, WARN, or BLOCK as a pre-install security signal and review findings before installing or updating a skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daririnch/skills/dcl-skill-auditor) <br>
- [DCL Trust Oracle MCP endpoint](https://mcp.fronesislabs.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, configuration, guidance] <br>
**Output Format:** [Structured JSON audit report with Markdown guidance and optional MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes PASS/WARN/BLOCK verdict, risk score, findings, content hashes, a deterministic audit proof, and an optional live-check transaction hash when the paid check is used.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
