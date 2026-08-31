## Description:

Helps agents discover, inspect, and run Monid data endpoints for social media, search, scraping, enrichment, and other structured data retrieval tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monid](https://clawhub.ai/user/monid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find available Monid endpoints, inspect their schemas, execute data runs, and retrieve results instead of building custom scrapers or assuming data is inaccessible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route broad tasks to external Monid services, including paid endpoints.

Mitigation: Require confirmation before paid runs and prefer the user's existing dedicated services, API keys, or tools when they already cover the task.

Risk: The skill can upload local files and create shareable or signed remote URLs.

Mitigation: Confirm before uploading local files or creating public or signed URLs, and use conservative file retention and cleanup practices.

Risk: The skill instructs agents to replace or update the installed skill from monid.ai.

Mitigation: Review and scan the updated skill before enabling it for future sessions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/monid/skills/monid-skill)
- [Monid Skill Definition](https://monid.ai/SKILL.md)
- [Monid App](https://app.monid.ai)
- [Monid API Keys](https://app.monid.ai/access/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Monid CLI commands, endpoint schemas, run IDs, saved result-file paths, and cost or balance notes when relevant.]

## Skill Version(s):

0.1.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
