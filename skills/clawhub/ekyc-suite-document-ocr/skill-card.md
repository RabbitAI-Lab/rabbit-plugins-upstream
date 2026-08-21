## Description:

eKYC Suite Document OCR helps agents extract structured fields from consented Chinese ID card, bank card, driver's license, and vehicle license images for KYC and document-review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

External users, KYC operations teams, fintech document-review teams, and developers use this skill to submit an authorized document image to a configured eKYC Suite Cloud endpoint and receive OCR extraction for supported document types. It is scoped to OCR extraction and human-reviewed document workflows, not authenticity decisions or face/liveness checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted documents and OCR results may contain sensitive personal or financial data.

Mitigation: Process only authorized documents and apply consent, retention, access-control, masking, and human-review policies before use.

Risk: The skill sends the user-supplied document image to the operator-configured eKYC cloud endpoint.

Mitigation: Use only trusted HTTPS endpoints and configure EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY in an approved deployment environment.

Risk: Optional deployment-context environment variables can add source, client, workspace, or install metadata to requests.

Mitigation: Set optional context variables only when they are needed for the deployment and approved by policy.

Risk: OCR extraction can be incomplete, unreadable, or unsuitable for final high-impact decisions.

Mitigation: Do not guess missing fields; request clearer images when needed and route uncertain or high-impact cases to authorized human reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr)
- [ClawHub publisher profile](https://clawhub.ai/user/carochen112233-commits)
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-document-ocr-mcp)
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [Face Compare skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)
- [AI Guardian skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [Media Labeling skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON OCR responses from the configured backend]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces OCR extraction results for one supported document image per command; local files are base64 encoded before HTTPS submission.]

## Skill Version(s):

1.0.18 (source: server release metadata, SKILL.md frontmatter, and script client version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
