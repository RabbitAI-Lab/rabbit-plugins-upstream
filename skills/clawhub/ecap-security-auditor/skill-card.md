## Description: <br>
Security audit framework for AI agent skills, MCP servers, and packages that gives agents structured prompts, registry checks, integrity verification, and reporting workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[starbuck100](https://clawhub.ai/user/starbuck100) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to evaluate packages, skills, and MCP servers before installation or use, then produce structured security findings, trust guidance, and remediation-oriented reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect package source and contact a remote registry. <br>
Mitigation: Use it only in environments where package source inspection and registry lookups are acceptable, and review network destinations before use. <br>
Risk: Audit reports may be uploaded to a third-party registry. <br>
Mitigation: Review generated reports before upload and remove sensitive package details or credentials from report content. <br>
Risk: The skill can store an API key and documentation includes an exposed bearer token. <br>
Mitigation: Rotate any exposed sample token, keep credentials out of committed files, and prefer environment-managed secrets. <br>
Risk: Adversarial and test documents include commands that are evidence, not operational instructions. <br>
Mitigation: Do not run commands copied from test or adversarial documents unless independently reviewed for the current environment. <br>
Risk: Changing ECAP_REGISTRY_URL can redirect trust checks and uploads. <br>
Mitigation: Keep ECAP_REGISTRY_URL unset unless you control and trust the alternate registry. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/starbuck100/skills/ecap-security-auditor) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/starbuck100) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Audit prompt](artifact/prompts/audit-prompt.md) <br>
- [Review prompt](artifact/prompts/review-prompt.md) <br>
- [Trust Registry](https://skillaudit-api.vercel.app) <br>
- [Trust Registry leaderboard](https://skillaudit-api.vercel.app/leaderboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON report examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query a remote registry, verify file hashes, and produce audit reports or review guidance.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
