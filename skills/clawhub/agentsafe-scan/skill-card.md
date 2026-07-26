## Description: <br>
Habit gate: before every remote skill install, re-fetch, or allowlist promotion, call a hosted heuristic static red-flag scan for risky shell, obfuscation, credential, staging, and outbound-call patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[albin-holmgren](https://clawhub.ai/user/albin-holmgren) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to check remote skill URLs or pasted skill markdown before installation, update, refetch, or allowlist promotion. It returns advisory static-scan results and next-action guidance for deny, review, allow-with-caution, payment, and drift workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scan requests may send skill URLs or pasted skill content to the hosted AgentSafe API. <br>
Mitigation: Use only content appropriate for that external service, and do not include secrets, credentials, private files, or personal data in payloads. <br>
Risk: Static scan results are advisory and can miss unsafe behavior or flag benign content. <br>
Mitigation: Treat low scores as insufficient proof of safety; require human review for review or deny decisions and install with least privilege when allowed. <br>
Risk: Remote skill content can drift after initial review. <br>
Mitigation: Use the content fingerprint and watch or rescan workflow before re-allowlisting changed remote content. <br>
Risk: Using the hosted service beyond the free quota can trigger paid Base USDC flows. <br>
Mitigation: Review quota and payment next-action fields before sending payment transactions, and keep ClawHub discovery separate from API-host billing. <br>


## Reference(s): <br>
- [AgentSafe Scan ClawHub listing](https://clawhub.ai/albin-holmgren/skills/agentsafe-scan) <br>
- [AgentSafe hosted API](https://agentsafe.up.railway.app) <br>
- [OpenAPI documentation](https://agentsafe.up.railway.app/docs) <br>
- [Agent brief](https://agentsafe.up.railway.app/llms.txt) <br>
- [API quick map](references/api-quick.md) <br>
- [Free to paid flow](references/payment.md) <br>
- [Example scan request](examples/scan-request.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Configuration] <br>
**Output Format:** [Markdown guidance with curl commands and JSON request or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory static-scan decisions, risk bands, findings, content fingerprints, capability signals, quota status, payment next steps, and watch or rescan guidance.] <br>

## Skill Version(s): <br>
0.1.8 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
