## Description:

爬虫网页 helps agents collect webpage content with Python and Scrapling-style simple selectors for data extraction and information gathering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and automation teams use this skill to ask an agent to collect webpage content with simple selectors and return scraping results for research, reporting, or workflow inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, exec, and glob access for a narrow webpage scraping purpose.

Mitigation: Run it only in a controlled workspace and grant the minimum file, command, and network scope required for the specific scraping task.

Risk: Web scraping can violate site terms, robots.txt, copyright restrictions, or rate limits.

Mitigation: Confirm authorization, follow target-site rules, and throttle requests before using the skill against a website.

Risk: Scraped pages, command output, or configured credentials may expose sensitive data.

Mitigation: Avoid scraping sensitive sources and review or redact outputs before sharing, storing, or committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/scrape-web)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional JSON result examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include webpage scraping results, execution status, configuration steps, and follow-up troubleshooting guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
