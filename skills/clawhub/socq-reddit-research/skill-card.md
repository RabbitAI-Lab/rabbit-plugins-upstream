## Description:

Research public Reddit content, accounts, keywords, and performance data with SocQ through CLI, MCP, or REST workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to select SocQ Reddit endpoints, estimate credits, submit asynchronous collection tasks, paginate results, and report normalized public Reddit findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocQ API key for CLI, MCP, and REST requests.

Mitigation: Keep SOCQ_API_KEY in the environment and avoid placing it in prompts, URLs, shell history, or committed files.

Risk: SocQ requests can consume credits, especially for large-volume or multi-endpoint runs.

Mitigation: Review endpoint cost estimates and obtain user confirmation before paid large-volume or multi-endpoint submissions.

Risk: Asynchronous tasks can remain queued, fail, or return partial paginated coverage.

Mitigation: Preserve task IDs, inspect terminal task status and normalized errors, and label incomplete coverage when pagination stops early or a provider fails.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Reddit Platform](https://socq.ai/apis/reddit)
- [SocQ Reddit API Documentation](https://docs.socq.ai/api-manual/reddit)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, execution notes, task status, credit usage, normalized findings, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, result counts, raw export locations, and coverage limitations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
