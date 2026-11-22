## Description:

Search publicly available WeChat articles and videos by keyword and return structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and analysts use this skill to find public WeChat articles and videos by keyword for content research and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to the third-party Guaikei API.

Mitigation: Use public, non-sensitive keywords and review the service terms before querying.

Risk: The security assessment is benign with medium confidence because only 18 of 28 components were fully inspected and tool-misuse analysis was degraded.

Mitigation: Review the skill before installation and account for the remaining uncertainty.

Risk: The API token could be exposed if included in command arguments or logs.

Mitigation: Keep GUAIKEI_API_TOKEN in the environment and never place it in command-line arguments.

## Reference(s):

- [Options reference](references/options.md)
- [FAQ and setup guidance](references/faq.md)
- [Changelog](references/changelog.md)
- [Guaikei API access and support](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON search results with usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14+ and GUAIKEI_API_TOKEN; searches public WeChat content.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
