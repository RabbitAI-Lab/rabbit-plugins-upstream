## Description: <br>
eKYC Suite Document OCR helps agents extract structured fields from consented Chinese ID card, bank card, driver's license, and vehicle license images for KYC onboarding and human-reviewed document workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, KYC onboarding teams, identity operations teams, and fintech document reviewers use this skill to extract structured OCR fields from supported, consented document images. It is intended for human-reviewed document workflows and not for unsupported OCR categories, authenticity proof, or final high-impact decisions without review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted document images and OCR results can contain sensitive identity or bank-card data. <br>
Mitigation: Use the skill only with authorization, and apply masking, access controls, retention limits, and human review before sharing results. <br>
Risk: The skill sends submitted media to the operator-configured eKYC backend for extraction. <br>
Mitigation: Install and run it only when the configured HTTPS backend is trusted and approved for the intended document-processing workflow. <br>
Risk: OCR extraction can be incomplete or unsuitable for final high-impact decisions. <br>
Mitigation: Do not guess missing fields; request clearer images when needed and route uncertain or high-impact cases to an authorized human reviewer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-document-ocr-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [Related Face Compare skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [Related AI Guardian skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [Related Media Labeling skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON OCR responses plus concise Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns backend-provided extracted fields without guessing missing or unreadable values; sensitive fields should be masked in user-facing summaries.] <br>

## Skill Version(s): <br>
1.0.12 (source: frontmatter and changelog, released 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
