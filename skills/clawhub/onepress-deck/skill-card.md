## Description:

Creates presentation decks as local HTML files or, with a OnePress API key, delegates deck creation to OnePress for cited research and export options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getonepress](https://clawhub.ai/user/getonepress)

### License/Terms of Use:

MIT

## Use Case:

Professionals and teams use this skill to create pitch decks, investor updates, board presentations, sales decks, and research briefings. Without an API key it writes a local HTML deck; with a key it submits the request to OnePress for a hosted deck and additional export options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When an API key is configured, deck prompts and follow-ups are sent to OnePress and may remain in its workspace.

Mitigation: Avoid submitting secrets, regulated data, or confidential business material unless OnePress is approved for that data; use local mode otherwise.

## Reference(s):

- [OnePress Deck on ClawHub](https://clawhub.ai/getonepress/skills/onepress-deck)
- [OnePress](https://www.getonepress.com)
- [OnePress workspace](https://www.getonepress.com/app)

## Skill Output:

**Output Type(s):** [HTML, Markdown, Guidance]

**Output Format:** [Local HTML slide deck or Markdown summary with a hosted workspace path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local decks include slide navigation; connected-mode exports are available through the OnePress workspace.]

## Skill Version(s):

3.0.2 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
