## Description:

This skill helps WeChat Official Account operators plan, generate, review, package, and optionally publish sticker-style or multi-image posts, including nine-grid layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External WeChat Official Account operators, self-media teams, and IP account maintainers use this skill to turn a topic or source material into a consistent set of image-led posts with captions, prompts, generated images, review checks, and optional WeChat publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send image prompts to an external image model API and upload generated image files to WeChat when publication is used.

Mitigation: Review the generated plan, prompts, and images before publication, and only run the publishing path when the intended WeChat account and content are confirmed.

Risk: The workflow requires image-model and WeChat app credentials.

Mitigation: Keep aws.env limited to the required API keys and WeChat application credentials, and scope those credentials to the accounts needed for this workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-sticker)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [Declared project homepage](https://aiworkskills.cn)
- [Declared source repository](https://github.com/aiworkskills/wechat-article-skills)
- [Sticker workflow reference](references/workflow.md)
- [Sticker review checklist](references/checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, configuration checks, generated prompt files, image files, and review checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update imgs/ assets, imgs/outline.md, prompt markdown files, and article status metadata during the workflow.]

## Skill Version(s):

1.0.24 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
