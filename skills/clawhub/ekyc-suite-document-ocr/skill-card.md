## Description: <br>
eKYC Suite Document OCR helps agents extract structured fields from consented Chinese ID cards, bank cards, driver's licenses, and vehicle licenses for KYC onboarding and human-reviewed document workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External teams, KYC operators, fintech identity reviewers, and integration developers use this skill to submit authorized document images to a configured eKYC Suite Cloud endpoint and receive structured OCR results for review. It is scoped to supported Chinese national ID cards, bank cards, driver's licenses, and vehicle licenses, and should not be used as final proof of document authenticity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document images and OCR results can contain sensitive personal data. <br>
Mitigation: Process only authorized images, use a trusted HTTPS eKYC Cloud endpoint, apply masking and access controls, and enforce retention limits. <br>
Risk: OCR extraction can be incomplete or inaccurate and does not prove document authenticity. <br>
Mitigation: Route uncertain or high-impact cases to an authorized human reviewer and avoid final decisions based only on OCR output. <br>
Risk: Optional source, client, workspace, or install headers may expose sensitive deployment context if misused. <br>
Mitigation: Avoid secrets or personal data in optional metadata and send only the operational context needed for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Document OCR MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-document-ocr-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite AI Guardian skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Media Labeling skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text, Shell commands, Configuration] <br>
**Output Format:** [JSON responses from the OCR client, with Markdown or shell command guidance from the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; accepts one user-supplied local file path, public HTTPS URL, or base64 document image.] <br>

## Skill Version(s): <br>
1.0.14 (source: frontmatter, changelog, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
