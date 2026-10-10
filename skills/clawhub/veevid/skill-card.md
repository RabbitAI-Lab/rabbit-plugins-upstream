## Description:

Guides an agent through Veevid's API to generate or edit video, images, and audio, with a price quote and user confirmation before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meigesir](https://clawhub.ai/user/meigesir)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose Veevid models, obtain a credit quote, and generate or edit video, images, speech, music, or transcripts after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media and prompts may contain sensitive personal information and are sent to Veevid and possibly downstream model providers.

Mitigation: Obtain consent before uploading personal photos, voices, or intimate media; avoid confidential documents and private URLs, and review service privacy and retention terms.

Risk: An exposed API key could permit unauthorized use of the account.

Mitigation: Protect the local API key file and avoid sharing the key in messages or public output.

Risk: Generation may consume credits, and listing past creations or deleting content can expose or alter user data.

Mitigation: Show the exact credit quote and obtain approval before generation; require explicit confirmation before listing past creations or deleting anything.

## Reference(s):

- [Veevid ClawHub release](https://clawhub.ai/meigesir/skills/veevid)
- [Veevid API key settings](https://veevid.ai/settings/api-keys)
- [Veevid API reference](references/api-reference.md)
- [Video model reference](references/models-video.md)
- [Image model reference](references/models-image.md)
- [Audio model reference](references/models-audio.md)
- [Video tools reference](references/models-tools.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with API request examples and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports quoted credit costs and requests user confirmation before generation.]

## Skill Version(s):

1.3.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
