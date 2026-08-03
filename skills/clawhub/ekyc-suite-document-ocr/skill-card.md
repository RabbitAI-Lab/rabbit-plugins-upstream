## Description: <br>
eKYC Suite Document OCR extracts structured fields from consented Chinese national ID cards, bank cards, driver's licenses, and vehicle licenses for KYC and eKYC document review workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External teams and agents use this skill to submit authorized document images for structured OCR extraction during KYC onboarding, eKYC onboarding, and human-reviewed document verification workflows. It is intended for supported document categories only and not for final high-impact decisions without review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document images and OCR results may contain sensitive identity or card data. <br>
Mitigation: Process only authorized images and apply masking, access control, retention limits, and human review for sensitive outputs. <br>
Risk: The skill sends user-supplied document images to the configured HTTPS OCR endpoint. <br>
Mitigation: Install only when the endpoint is trusted and the operator has appropriate consent, privacy, and retention controls. <br>
Risk: Optional client, workspace, source, or install context variables can add deployment metadata to requests. <br>
Mitigation: Set optional context variables only when they are needed for the deployment. <br>
Risk: OCR extraction does not prove document authenticity or suitability for a final eligibility decision. <br>
Mitigation: Route uncertain or high-impact cases to an authorized human reviewer and combine OCR with the operator's validation controls. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [Related MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-document-ocr-mcp) <br>
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON OCR responses with human-facing text or Markdown summaries and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns extracted fields from the configured OCR service; user-facing summaries should mask sensitive document and card data.] <br>

## Skill Version(s): <br>
1.0.15 (source: frontmatter, changelog, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
