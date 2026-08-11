## Description: <br>
Audit a named ClawHub skill or skill URL before installation by combining OpenClaw verification with bounded static analysis. Use when the user explicitly asks whether a skill is safe or requests a pre-install review; report evidence and uncertainty instead of treating a score as proof. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit ClawHub skills before installation, combining registry verification with bounded static analysis and clear uncertainty reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit scores and clean findings are advisory and can be mistaken for proof that a skill is safe. <br>
Mitigation: Present the registry decision, exact-version evidence, and any uncertainty; require separate user authorization before installation. <br>
Risk: Optional LLM review can send selected excerpts and flagged context to Anthropic. <br>
Mitigation: Avoid --llm for private or sensitive skill material unless the user accepts that disclosure. <br>
Risk: Incomplete scans or fetch failures can leave files unreviewed. <br>
Mitigation: Treat incomplete scans as UNKNOWN and inspect the exact release files before proceeding. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jonathanjing/skills/skill-trust-auditor) <br>
- [OpenClaw Homepage Metadata](https://clawhub.ai/jonathanjing/skill-trust-auditor) <br>
- [ClawHavoc Pattern Reference](references/clawhavoc-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Shell commands, JSON] <br>
**Output Format:** [Markdown summary with optional JSON audit report and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional --llm mode may send selected audit context to Anthropic; --json-only returns a machine-readable report.] <br>

## Skill Version(s): <br>
1.1.5 (source: SKILL.md metadata.openclaw.version, skill.json, CHANGELOG, and server release metadata; released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
