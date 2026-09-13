## Description:

Route broad search, scraping, monitoring, marketplace, social, travel, jobs, and maps requests to the smallest suitable Dataify skill set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate broad Dataify data collection requests into a minimal capability plan and route execution to suitable search, scraping, monitoring, marketplace, social, travel, jobs, or maps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User requests can submit Dataify data collection tasks that consume account credits.

Mitigation: Review broad, high-volume, multi-page, media-download, or materially credit-sensitive requests before proceeding.

Risk: The skill depends on a Dataify API token for authenticated workflows.

Mitigation: Read DATAIFY_API_TOKEN from the environment, verify presence without printing it, and never include tokens in commands or output.

Risk: Ambiguous collection goals can route to an unsuitable capability or source plan.

Mitigation: Restate the deliverable, target sources, scope, freshness, and output format, then ask only for missing required inputs or material ambiguities.

## Reference(s):

- [Dataify capability map](references/capability-map.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-router)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise Markdown with optional shell commands, source coverage, limitations, and asynchronous task state.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route work to external Dataify workflows and may return task IDs or collected results depending on request scope.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
