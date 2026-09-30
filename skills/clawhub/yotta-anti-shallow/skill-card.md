## Description:

Guides an agent to analyze complex tasks before acting, state uncertainty, and check its work without replacing tests or human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users apply these quality checks to complex analysis, writing, and coding tasks to encourage clear reasoning, uncertainty disclosure, and self-review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional installers write into agent skill directories, and bulk installation enables the rules for multiple agents.

Mitigation: Review the installer or pin the package version before installation; choose only the intended agent directories.

Risk: Analysis and confirmation steps can delay work or create a false sense that the response was verified.

Mitigation: Apply the rules in proportion to task complexity and independently test or review consequential results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [Project homepage](https://github.com/YottaMeta/yotta-anti-shallow)
- [Frequently asked questions](references/faq.md)
- [Example walkthroughs](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Code]

**Output Format:** [Markdown or plain text, depending on the user's task]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a brief plan, uncertainty statement, and self-check; the skill itself does not execute tools or verify results.]

## Skill Version(s):

1.4.1 (source: server release, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
