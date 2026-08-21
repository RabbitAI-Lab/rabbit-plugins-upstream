## Description:

Analyzes publicly accessible image URLs with LinkFox's multimodal API and returns textual image descriptions, OCR-style extraction, visual question answering, or product-image analysis based on the user's requirement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send a public image URL, optionally with a natural-language analysis requirement, and receive a text-based interpretation of image contents, visible text, or product imagery. It also guides API-key setup and credit handling for LinkFox-powered image analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs, local-image uploads, and recognition requirements are sent to LinkFox, and local image paths may be uploaded to public-read storage for temporary URL-based analysis.

Mitigation: Use only images that are appropriate to share with LinkFox; avoid confidential screenshots, documents, personal photos, regulated data, and private business images unless data-sharing and retention implications have been reviewed.

Risk: Full recognition results are written to local session files and may also be cached locally.

Mitigation: Run the skill in a workspace suitable for the image contents and clear generated linkfox data or cache files when results should not remain on disk.

Risk: The skill includes API-key, phone-login, credit, and payment helper flows.

Mitigation: Confirm that users intend to use LinkFox account and billing flows before onboarding, ordering credits, or configuring API keys.

Risk: Image recognition calls consume LinkFox credits and the artifact notes that dynamic charging can consume a large number of credits.

Mitigation: Tell the user before additional calls that credits may be consumed, and avoid repeated retries or parameter changes unless the user confirms.

## Reference(s):

- [图片识别 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-recognize-image)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, stdout summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are persisted under a local linkfox session directory; small responses may also print in full to stdout, while larger responses print a summary unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
