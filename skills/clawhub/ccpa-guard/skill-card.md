## Description: <br>
CCPA Guardrail is a local runtime guardrail that detects, masks, or blocks CCPA/CPRA-oriented US and California personal data in AI application inputs and outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to add a local PII guardrail around agent input and output flows, returning structured decisions for detect, mask, or block actions. Treat it as an auxiliary privacy control, not as legal advice or proof of compliance. <br>

### Deployment Geography for Use: <br>
Global; intended data-protection profile is CCPA/CPRA for US and California personal data. <br>

## Known Risks and Mitigations: <br>
Risk: Documentation and release claims mix GDPR and CCPA terminology while the implemented profile is CCPA-oriented, which can lead users to rely on the wrong regulatory coverage. <br>
Mitigation: Use the skill only for local CCPA/US-California PII masking until the publisher aligns the name, documentation, metadata, implemented rules, and tests. <br>
Risk: Regex and keyword detection can miss personal data or produce false positives, especially outside the documented CCPA/CPRA categories. <br>
Mitigation: Treat results as an auxiliary control, test against representative application data, and keep legal or compliance review for material decisions. <br>
Risk: Passing sensitive text through command-line arguments can expose it through shell history, process listings, or logs even though the tool itself runs locally. <br>
Mitigation: Prefer standard input or controlled agent plumbing for sensitive content, and avoid logging raw inputs or unmasked outputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wwumit/skills/ccpa-guard) <br>
- [README.md](README.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or structured JSON from CLI guardrail checks; Markdown guidance in skill instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-only execution; supports detect, mask, and block actions with risk levels and finding previews.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
