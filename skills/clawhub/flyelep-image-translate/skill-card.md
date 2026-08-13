## Description:

Uses the Flyelep AI Tool API to identify and translate text in an image, returning a URL for the translated image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate text embedded in posters, product images, and other public image URLs through Flyelep's API after providing an API key, image URL, and target language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API request sends the user-provided image URL and translation request to Flyelep.

Mitigation: Use a dedicated Flyelep API key and avoid submitting private or sensitive images.

Risk: Image URLs can expose access tokens, confidential paths, or business data.

Mitigation: Use public direct image URLs that do not contain credentials, expiring access tokens, or confidential identifiers.

Risk: A missing, invalid, or overprivileged Flyelep secretKey can cause failed requests or unnecessary credential exposure.

Mitigation: Provide the secretKey only at runtime in the request header and do not store real keys in skill files, examples, repositories, or persistent configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-image-translate)
- [Flyelep image translation API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/translate)
- [Flyelep open platform dashboard](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with JSON request examples and a translated image URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Flyelep secretKey and a public direct image URL; returns the translated image URL without rereading image contents.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
