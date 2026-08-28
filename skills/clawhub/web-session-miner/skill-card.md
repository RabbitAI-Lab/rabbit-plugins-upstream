## Description:

Web Session Miner guides agents to use an already authorized browser session and site-specific recipes to collect web-visible business and profile data into structured outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and business users use this skill to automate authorized collection from websites where the user is already logged in, including supplier checks, ownership tracing, investment diligence, and competitive research. It is intended for data the user is permitted to access and for reports that preserve source, time, and data-range context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated collection through logged-in browser sessions can violate site terms or account permissions if used outside authorized access.

Mitigation: Use only on accounts and sites where the user has explicit permission, check site terms and robots requirements, and prefer official APIs where contractually required.

Risk: Using paid or member web access to avoid API charges may breach data-provider contracts or replace licensed programmatic access.

Mitigation: Do not use it to replace paid programmatic access or scrape member-only data at scale without authorization; obtain approval for each target data source.

Risk: Browser-session automation may expose cookies, personal data, or high-privilege account data.

Mitigation: Use a dedicated low-privilege browser profile, avoid sensitive accounts, limit the collection scope, and stop browser sessions after collection.

Risk: Scraped pages can be incomplete, stale, or affected by pagination, login expiry, anti-automation controls, or ambiguous entities.

Mitigation: Record source site, login-state source, capture time, data range, and unresolved ambiguity in every report; verify critical fields against official sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiyanjun/skills/web-session-miner)
- [Artifact SKILL.md](artifact/SKILL.md)
- [Artifact README.md](artifact/README.md)
- [Qichacha recipe](artifact/recipes/qcc.md)
- [Tianyancha recipe](artifact/recipes/tyc.md)
- [Data sanitization audit](artifact/AUDIT.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON, Markdown, HTML reports]

**Output Format:** [Markdown guidance with inline shell and JavaScript snippets; extracted results may be JSON, Markdown, or HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify the source site, login-state source, capture time, and data range; site adapters may require browser-skill and an active logged-in browser session.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
