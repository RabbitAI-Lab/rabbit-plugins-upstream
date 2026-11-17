## Description:

Search meme templates, suggest formats, and generate local or hosted image memes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can search a curated meme-template registry, get format suggestions for a topic, and create local or hosted meme drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imgflip hosted rendering sends meme captions to an external service and uses account credentials.

Mitigation: Use local rendering for private captions, and keep Imgflip credentials private; avoid supplying them on command lines where shell history or process listings may expose them.

## Reference(s):

- [Curated meme template registry](artifact/references/templates.json)
- [ClawHub skill page](https://clawhub.ai/hillstreet-ph/skills/meme-maker)
- [Drakeposting template background](https://knowyourmeme.com/memes/drakeposting)

## Skill Output:

**Output Type(s):** [Image files, Text, URLs, JSON]

**Output Format:** [SVG or PNG meme images, hosted image URLs, and optional JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local SVG is the default render; PNG requires Playwright Chromium or Google Chrome. Hosted Imgflip rendering requires user credentials.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
