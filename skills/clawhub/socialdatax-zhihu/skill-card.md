## Description:

Helps agents research Zhihu trends, content, discussions, and creators using SocialDataX data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to review Zhihu hot lists, search and inspect content, analyze comments, and examine creator profiles and posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended runtime command fetches an unpinned npm package that can access the SocialDataX API key.

Mitigation: Review and pin the package version or use a controlled local installation before supplying the API key; avoid unnecessary local execution permissions.

## Reference(s):

- [SocialDataX Zhihu skill on ClawHub](https://clawhub.ai/devinchen2014/skills/socialdatax-zhihu)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with optional CLI commands and data excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Zhihu lookups; requires a SocialDataX API key.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
