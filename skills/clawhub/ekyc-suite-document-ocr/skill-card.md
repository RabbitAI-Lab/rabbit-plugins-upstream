## Description: <br>
eKYC Suite Document OCR helps agents extract structured fields from consented Chinese ID cards, bank cards, driver's licenses, and vehicle licenses through a configured eKYC cloud OCR service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and KYC operations teams use this skill to run structured OCR extraction for supported document images during consent-based onboarding and document review. Results should support human-reviewed workflows rather than final high-impact decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Identity and financial document images are sent to the configured eKYC cloud endpoint and may contain sensitive personal data. <br>
Mitigation: Process only authorized images and enforce retention, masking, access-control, and human-review rules before use. <br>
Risk: OCR output may be incomplete or incorrect and does not establish document authenticity. <br>
Mitigation: Use the skill only for the supported document categories, avoid guessing missing fields, and route uncertain or high-impact cases to an authorized reviewer. <br>
Risk: Optional context environment variables could expose sensitive identifiers if operators place secrets or personal data in them. <br>
Mitigation: Keep secrets, tokens, personal data, and internal sensitive identifiers out of optional context variables. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-document-ocr-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON OCR responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an operator-configured HTTPS endpoint and API key; local image inputs are encoded before transmission.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
