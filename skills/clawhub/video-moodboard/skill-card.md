## Description:

Creates a measurable moodboard for AI image and video models and checks its specifications on test stills before video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video teams use the skill to turn a visual brief and selected references into a quantified moodboard, a visual board, and evaluated test stills before generating video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Test generation sends prompts and attached reference images to the selected provider and may incur costs.

Mitigation: Use content you are comfortable sharing and confirm provider pricing before generating test stills.

Risk: The HTML board loads remote fonts and images.

Mitigation: Review remote assets before opening or sharing the board, and use offline alternatives when needed.

Risk: Installation or connected services can execute external code or send data.

Mitigation: Use a single-skill install and reviewed, pinned installer and repository versions; external services were not executed during static review.

## Reference(s):

- [Declared skill homepage](https://github.com/vargHQ/skills/tree/main/video-moodboard)
- [Moodboard test evidence](https://claude.ai/artifact/5ptKSPYFzvd7turkZevfHZ)
- [Evidence behind the ranking](references/evidence.md)
- [Moodboard template](references/moodboard-template.md)
- [Judging test stills](references/judge.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Images, Analysis]

**Output Format:** [Markdown moodboard and checks, an HTML visual board, and image test stills]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Test still generation may use paid provider services; reference images should be rights-cleared.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
