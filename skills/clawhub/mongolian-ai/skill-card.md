## Description:

Helps agents translate, converse, recognize text and speech, synthesize speech, and translate documents in Traditional and Cyrillic Mongolian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use the skill to translate Chinese and Mongolian text, draft Mongolian-language responses, extract text from images or audio, generate speech, and translate DOCX or PDF content through the AI Skills platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested text, images, audio, and documents are sent to the external AI Skills platform.

Mitigation: Submit only user-authorized material; do not send confidential or regulated content without organizational approval of the vendor.

Risk: Processing can charge the platform wallet, particularly for large or multi-step requests.

Mitigation: Confirm the scope of costly requests and reuse the same idempotency key when retrying an unchanged request.

Risk: Exposing the platform API key could permit unauthorized use.

Mitigation: Keep the key in its environment variable and out of logs, screenshots, and chat replies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/youteacher/skills/mongolian-ai)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/INTERFACE-ROUTING.md)
- [Translation reference](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/TRANSLATION.md)
- [API key setup](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/API-KEY.md)

## Skill Output:

**Output Type(s):** [Text, Audio files]

**Output Format:** [Plain text and WAV, MP3, or OGG audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report platform wallet charges; document translation yields text, not a reformatted document.]

## Skill Version(s):

2.0.5 (source: server release and packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
