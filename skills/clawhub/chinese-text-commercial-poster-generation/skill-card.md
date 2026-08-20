## Description:

Uses AI Hive GPT Image 2 to generate commercial images with approved Chinese, English, numeric, and punctuation copy by layout zone, with offline character audits and targeted typo repair to reduce text errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, ecommerce, and design teams use this skill to turn approved copy contracts into Chinese commercial posters, product feature cards, campaign key visuals, social covers, bilingual ads, and package-front concepts. Operators can audit transcribed or OCR-confirmed output text offline and request local repair for observed text mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images named in commands are uploaded to AI Hive for generation.

Mitigation: Use only approved source images and install the skill only when sharing those selected images with AI Hive is acceptable.

Risk: Generated text may be wrong or unsuitable for mandatory content such as prices, dates, legal text, packaging claims, or QR codes.

Mitigation: Treat generated images as drafts and manually verify mandatory content before publication.

Risk: Use requires an AI Hive API key.

Mitigation: Provide the key only through the documented command, environment variable, or local configuration path and manage it as a credential.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/chinese-text-commercial-poster-generation)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON audit output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are created through AI Hive from user-selected source images; audit output is local JSON.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
