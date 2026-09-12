## Description:

Compare advertised hiring demand across roles, skills, locations, and seniority using Crawlora's jobs dataset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Crawlora's jobs dataset and report hiring-demand snapshots across roles, skills, locations, seniority, employers, remote-work status, and advertised compensation. It guides analyses toward explicit denominators, coverage notes, deduplication, and limits on trend or labor-market claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key.

Mitigation: Keep the key scoped to Crawlora, store it in CRAWLORA_API_KEY, and avoid exposing it in prompts, logs, command history, or shared outputs.

Risk: Job-search queries and POST bodies are sent to Crawlora's API.

Mitigation: Avoid placing unrelated private data in query parameters or request bodies, and use the skill only when that data transfer is acceptable.

Risk: Observed job postings can be mistaken for completed hires, total labor-market demand, or point-in-time historical vacancies.

Mitigation: Report the cohort definition, coverage, exclusions, deduplication method, denominator, sample truncation, and limitations with every analysis.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/hiring-demand-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and should report query scope, coverage, denominators, counts, proportions, example postings, and limitations.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
