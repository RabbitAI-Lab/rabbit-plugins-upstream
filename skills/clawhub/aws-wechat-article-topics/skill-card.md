## Description:

Helps WeChat public-account editors research article topics, generate headline and summary options, and plan single articles or series.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

Content editors and operations teams use this skill to research WeChat public-account topic ideas, compare angles, generate headline and digest candidates, and plan article series before drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can alter article metadata or add related-article links to publishable content.

Mitigation: Review metadata changes and approve every related-article URL before publishing.

Risk: Related-link insertion is described as using an unaudited sibling script.

Mitigation: Treat related-link insertion as a publishing action and run it only where generated changes can be inspected before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-topics)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [Skill homepage](https://aiworkskills.cn)
- [Source repository](https://github.com/aiworkskills/wechat-article-skills)
- [Output format reference](artifact/references/output-format.md)
- [Research strategy reference](artifact/references/research-strategy.md)
- [Title presets reference](artifact/references/title-presets.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown topic cards, research summaries, YAML metadata updates, and occasional Python shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update topic-card.md, research.md, and article.yaml in the article workspace.]

## Skill Version(s):

1.0.25 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
