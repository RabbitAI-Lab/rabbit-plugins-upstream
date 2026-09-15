## Description:

Generates a Sogou Input Method hot-word or meme-style keyboard skin background from a user-provided image and optional style description, then returns the generated image with a fixed campus AI creative skin contest page link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

External users run this skill in an AI client when they want to turn an uploaded image into a styled Sogou keyboard skin or background. The skill guides image-to-image prompt construction, applies documented content guardrails, and returns the generated image with a fixed contest-detail link for the user to open manually.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The result includes a fixed external promotional contest link.

Mitigation: Present the link as an external contest-detail page and rely on the user to open it only when they intend to view the contest.

Risk: A user style request could conflict with the image-generation guardrails.

Mitigation: Apply the documented prompt-sanitization flow and hard content boundaries before image generation.

## Reference(s):

- [Generation Prompt Reference](references/generation-prompt.md)
- [Campus AI Creative Skin Contest Page](https://pinyin.sginput.qq.com/h5/kaixueskill/share/225448950305128448)

## Skill Output:

**Output Type(s):** [image, text, guidance]

**Output Format:** [Generated image plus concise text containing a fixed external contest link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires one uploaded image and accepts an optional style description; the external page is returned for manual user opening.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
