## Description:

Trae-Hot guides agents through a TRAE AI Creativity Contest submission workflow, from topic selection and registration posts through HTML product pages, preliminary posts, mock judging, video scripts, scoring prediction, and post-publication review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pandleeai](https://clawhub.ai/user/pandleeai)

### License/Terms of Use:

MIT

## Use Case:

External creators and developers use this skill to plan and produce TRAE AI Creativity Contest submissions, including contest posts, product-page HTML, mock judging notes, video scripts, scoring predictions, and review artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow tracks account and demo state and prepares public contest content that may include TRAE Session IDs.

Mitigation: Keep state.md private, review generated public posts before publishing, and redact sensitive identifiers wherever contest rules allow.

Risk: Keyword-based activation can start the contest workflow when a user did not intend to create submission materials.

Mitigation: Use explicit TRAE contest prompts and confirm before creating, updating, or publishing demo materials.

## Reference(s):

- [Server-resolved source repository](https://github.com/PandLeeAI/TraeHot)
- [ClawHub skill page](https://clawhub.ai/pandleeai/skills/traehot)
- [TRAE AI Creativity Contest page](https://www.trae.cn/ai-creativity?utm_source=community)
- [TRAE contest forum category](https://forum.trae.cn/c/38-category/38)
- [TRAE contest rules guide](https://forum.trae.cn/t/topic/22547)
- [TRAE registration guide](https://forum.trae.cn/t/topic/22548)
- [TRAE preliminary round guide](https://forum.trae.cn/t/topic/22549)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, generated contest copy, single-file HTML, and local file paths or shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged local demo materials and may update local state when used as directed.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
