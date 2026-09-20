## Description:

Generates daily Xiaohongshu-style Chinese health and wellness notes around 800 Chinese characters, using emoji-heavy checklist formatting, rotating title formulas, compliant in-platform calls to action, hashtags, optional local saving, and a helper script that indexes drafted Markdown notes into an HTML article library.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meimei-shoulu](https://clawhub.ai/user/meimei-shoulu)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, Xiaohongshu health bloggers, and social content operators use this skill to draft one compliant Chinese health-and-wellness note per day with short-line formatting, hashtags, and platform-safe calls to action. Agents can also save drafted Markdown notes into a dated notes directory and add them to a local HTML article library when the user provides a target path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated health content could include misleading, overconfident, or unsupported wellness claims.

Mitigation: Review each note before publishing and remove absolute efficacy language, invented medical details, specific drug or hospital names, and claims that require professional validation.

Risk: Xiaohongshu posts can be penalized if they include off-platform contact details or prohibited lead-generation language.

Mitigation: Run the skill's red-line self-check on every draft and keep calls to action limited to in-platform following, collection, comments, or official group chat flows.

Risk: The helper script writes to a local HTML article library based on the note path or a provided library path.

Mitigation: Choose the notes directory deliberately, review the generated Markdown path before indexing, and run the script only against content intended for that local library.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/meimei-shoulu/skills/health-xhs-daily)
- [Publisher profile](https://clawhub.ai/user/meimei-shoulu)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Chinese Markdown note drafts with optional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts target 600-1000 Chinese characters, use short mobile-friendly lines, include 5-8 hashtags with #女性健康, avoid medical certainty claims and off-platform contact details, and may be saved as dated Markdown files before local HTML indexing.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
