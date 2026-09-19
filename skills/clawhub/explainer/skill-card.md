## Description:

Turns supplied writing into a short Ofox-generated explainer video by selecting one concrete idea, drafting spoken words, estimating cost, and delegating generation to ofox-video-core.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn an article, document, release note, or paper into a short spoken explainer clip. It is best suited to choosing one idea that can stand alone, writing the spoken script, showing cost before paid generation, and returning the generated video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates execution to external Ofox skill components with broad, unpinned authority.

Mitigation: Use only after trusting the Ofox publisher, pin and review the exact ofox-video-core version, and scan the installed skill before deployment.

Risk: OFOX_API_KEY is used for paid API requests and generated prompts.

Mitigation: Keep the key narrowly scoped, avoid exposing secrets in prompts or logs, and require the cost estimate and user approval before submitting a paid generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/explainer)
- [Explainer source homepage](https://github.com/ofoxai/skills/tree/main/skills/explainer)
- [Ofox API keys](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command blocks, generated prompt text, cost estimates, and job result fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Ofox job details and an absolute VIDEO_PATH after successful generation.]

## Skill Version(s):

1.1.2 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
