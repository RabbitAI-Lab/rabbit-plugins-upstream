## Description:

Turn a slide deck or topic into a narrated explainer video with AI narration and an MP4 download through OnePress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getonepress](https://clawhub.ai/user/getonepress)

### License/Terms of Use:

MIT

## Use Case:

Creators and teams use this skill to turn slide decks, pitches, and research briefings into narrated videos and save the resulting MP4 locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decks, prompts, and uploaded voice samples are sent to OnePress for processing.

Mitigation: Upload only material the user is comfortable sharing with OnePress.

Risk: An exposed account key could grant unintended OnePress access.

Mitigation: Keep ONEPRESS_API_KEY in the host secret or environment store, never in chat or logs, and revoke it in OnePress settings if needed.

Risk: Downloading an MP4 to an unsuitable path could overwrite a local file.

Mitigation: Choose a safe output filename and folder before downloading.

## Reference(s):

- [OnePress](https://www.getonepress.com)
- [OnePress Deck Video on ClawHub](https://clawhub.ai/getonepress/skills/onepress-deck-video)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Text response and downloaded MP4 file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports a task summary, conversation ID, and local MP4 path.]

## Skill Version(s):

1.1.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
