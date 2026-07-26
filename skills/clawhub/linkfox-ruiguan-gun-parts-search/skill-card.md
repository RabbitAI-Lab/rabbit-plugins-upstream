## Description: <br>
Screens publicly accessible product image URLs with Ruiguan image similarity search to identify potential product policy-compliance violations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace operators, and compliance reviewers use this skill to pre-screen product images for similarity to known prohibited or policy-violating items before listing or review. It presents detection results as compliance signals, not legal conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product images and related user content are sent to LinkFox services for compliance checking. <br>
Mitigation: Use the skill only with images the user is comfortable sharing with LinkFox, and avoid private or unreleased product images unless that exposure is acceptable. <br>
Risk: Local image files are uploaded to obtain a public URL that is valid for a limited time. <br>
Mitigation: Confirm that temporary public exposure is acceptable before uploading local files, and prefer already public product-image URLs when possible. <br>
Risk: The skill consumes paid credits and stores full response data locally. <br>
Mitigation: Inform users before repeated or batch checks, rely on the built-in cache for duplicate requests, and review saved response files for sensitive result data. <br>


## Reference(s): <br>
- [睿观-图片合规检测 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-gun-parts-search) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Files, JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns matched violation records with image URLs, similarity scores, titles, detection IDs, and token cost; large responses are summarized after the full JSON is saved locally.] <br>

## Skill Version(s): <br>
1.0.4 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
