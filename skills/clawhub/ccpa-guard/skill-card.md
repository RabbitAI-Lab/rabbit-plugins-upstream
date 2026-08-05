## Description: <br>
CCPA Guardrail locally detects CCPA/CPRA personal information in agent inputs or outputs and returns risk-based detect, mask, or block decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to screen text before or after model calls for CCPA/CPRA personal information and apply detection, masking, or blocking decisions. It is intended as a local privacy guardrail, not as legal advice or a standalone compliance guarantee. <br>

### Deployment Geography for Use: <br>
United States, focused on California CCPA/CPRA privacy-law contexts <br>

## Known Risks and Mitigations: <br>
Risk: PII detection may produce false positives or miss personal information because rule and keyword matching cannot guarantee complete CCPA/CPRA coverage. <br>
Mitigation: Use the skill as one privacy safeguard within a broader compliance process and have qualified reviewers assess high-impact decisions. <br>
Risk: Real personal information may be present in inputs or outputs during agent workflows. <br>
Mitigation: Use mask or block mode for production handling of personal information and avoid logging unmasked source text. <br>
Risk: The skill can assist with privacy screening but does not establish legal compliance. <br>
Mitigation: Treat results as operational guidance and consult legal or compliance professionals for binding CCPA/CPRA obligations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ccpa-guard) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or structured JSON from a local command-line guardrail] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports detect, mask, and block actions; findings provide masked previews rather than original sensitive text.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
