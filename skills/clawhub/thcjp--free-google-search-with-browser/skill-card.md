## Description:

Guides an agent to perform scrapling-based Google searches and return structured results with titles, links, and snippets, with Chinese-language interaction support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators can use this skill to request Google search-result collection and receive structured search information for keyword research, SEO review, and general information retrieval. It is not suitable for black-hat SEO or illegal scraping use cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests shell-command capability without a concrete implementation or enforceable command scope.

Mitigation: Require the publisher to provide the actual search script plus a concrete command allowlist or wrapper before deployment.

Risk: Broad execution capability could expose sensitive files or credentials in the agent environment.

Mitigation: Run the skill in a sandboxed environment without sensitive files, credentials, or unnecessary filesystem access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/free-google-search-with-browser)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-style result examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected search-result data includes success status, structured data, and error details when available.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 0.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
