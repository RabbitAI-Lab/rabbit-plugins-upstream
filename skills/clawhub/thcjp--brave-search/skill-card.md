## Description:

Provides Brave Search API web search and content extraction for research, SEO analysis, data gathering, and workflow assistance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and workflow authors use this skill to search the web, extract content, gather research material, and support SEO or data-analysis tasks through Brave Search API results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents command execution and local file handling authority that is broader than normal web search requires.

Mitigation: Run it in a constrained agent profile and grant only the minimum tools needed for Brave Search queries.

Risk: Search prompts, context, or local files could contain confidential information.

Mitigation: Use only non-sensitive queries and avoid passing secrets, proprietary content, or local files to the skill.

Risk: API key configuration may expose credentials if handled carelessly.

Mitigation: Store API keys in environment variables or a secrets manager, avoid hardcoding them, and rotate credentials if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/brave-search)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown guidance with optional JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an API key and network access for Brave Search queries.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
