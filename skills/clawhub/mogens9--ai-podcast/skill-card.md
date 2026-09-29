## Description:

Generate AI podcast episodes from PDFs, text, notes, and links using MagicPodcast in OpenClaw.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mogens9](https://clawhub.ai/user/mogens9)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to turn PDF URLs, pasted text, notes, and links into two-person podcast episodes, then track progress and retrieve the finished share link from MagicPodcast.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided PDF URLs or pasted text are sent to MagicPodcast for processing.

Mitigation: Avoid confidential documents unless third-party processing is approved.

Risk: The skill requires a MagicPodcast API key.

Mitigation: Set the API key as an environment variable and avoid sharing it directly in chat.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mogens9/skills/ai-podcast)
- [MagicPodcast Homepage](https://www.magicpodcast.app)
- [MagicPodcast OpenClaw API Key Setup](https://www.magicpodcast.app/openclaw)
- [MagicPodcast Dashboard](https://www.magicpodcast.app/app)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command templates, status summaries, and podcast links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the MagicPodcast dashboard link after creation and a share URL, app URL fallback, or surfaced API error details when status is checked.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
