## Description:

Coordinates a WeChat official account content pipeline from topic selection through drafting, review, formatting, image preparation, and draft or publish handoff across the aws-wechat-article skill suite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External content editors, creators, and brand content teams use this skill to run a full WeChat article workflow, including setup checks, article planning, drafting, review, formatting, image preparation, and publishing handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured third-party WeChat API proxy may handle account credentials, tokens, article drafts, and publishing actions.

Mitigation: Review the skill before connecting a real WeChat account, and prefer the official WeChat endpoint unless the publisher's proxy is explicitly trusted.

Risk: Credential material for writing, image, and WeChat services could be exposed if local environment files are shared or committed.

Mitigation: Keep aws.env out of source control and use revocable, least-privilege credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-main)
- [Publisher Profile](https://clawhub.ai/user/aiworkskills)
- [AI Work Skills Setup Platform](https://aiworkskills.cn/)
- [First-Time Setup](artifact/references/first-time-setup.md)
- [Configuration and Article Schema](artifact/references/articlescreening-schema.md)
- [Configuration Example](artifact/references/config.example.yaml)
- [Environment Example](artifact/references/env.example.yaml)
- [Writing Specification Example](artifact/references/writing-spec.example.md)
- [Review Rules Example](artifact/references/presets/review-rules.example.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated article, configuration, and media workflow files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write workspace-local .aws-article configuration and per-article draft artifacts when the workflow is run.]

## Skill Version(s):

1.0.27 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
