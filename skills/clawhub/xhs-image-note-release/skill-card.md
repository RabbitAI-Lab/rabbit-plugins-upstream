## Description:

Automates Xiaohongshu image-note publishing through ego-browser and includes a configurable card generator for themed social image cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

External creators and agent users use this skill to generate Xiaohongshu-ready image cards, upload images, fill post text and topics, and publish image notes from an already logged-in Xiaohongshu account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically publish live Xiaohongshu posts from a logged-in account.

Mitigation: Use it only when live posting is intended, and review the title, body, images, and topics before running the publish flow.

Risk: The skill guidance may weaken normal sandbox boundaries around browser automation.

Mitigation: Do not disable sandboxing unless the browser session and file inputs are isolated and understood.

Risk: Untrusted SVG illustrations or topic values can affect generated cards or posted content.

Mitigation: Use trusted image assets and topic values that have been reviewed before generation or publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/xhs-image-note-release)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Publish method reference](references/publish-method.md)
- [Card generator reference implementation](references/card-generator/card_generator.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and JavaScript snippets; PNG image files when the card generator is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can automate browser actions against a live logged-in Xiaohongshu account and can generate 1080x1440 social image cards.]

## Skill Version(s):

1.5.2 (source: release evidence and changelog, released 2026-08-02)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
