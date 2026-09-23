## Description:

Reviews HTML for accessibility, form, semantic, SEO, validation, and performance issues, then provides practical fixes and guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and web teams use this skill to review HTML snippets or pages for accessibility, form labeling, semantic structure, SEO metadata, validation, and loading-strategy improvements. It returns issue summaries, repair suggestions, and example HTML or configuration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution and file-writing authority beyond a narrow HTML review workflow.

Mitigation: Run it in a restricted workspace and require explicit approval for command execution, file modification, and network or API access.

Risk: HTML fixes and SEO recommendations can change page behavior or introduce incorrect markup if applied automatically.

Mitigation: Review proposed changes before applying them and validate resulting pages with accessibility, HTML, and SEO checks.

Risk: Input HTML or page content may contain sensitive data.

Mitigation: Remove secrets, tokens, private customer data, and other sensitive values before sharing content with the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/html)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Schema.org structured data reference](https://schema.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with issue summaries, recommendations, and inline HTML, JSON, JavaScript, or shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity labels, fixed markup examples, validation notes, and follow-up troubleshooting steps.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
