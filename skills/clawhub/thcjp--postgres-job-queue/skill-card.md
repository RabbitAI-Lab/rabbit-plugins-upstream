## Description:

Helps developers design and implement a PostgreSQL-backed job queue with priority scheduling, batch claiming, retry handling, stale-job recovery, and progress tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design PostgreSQL-backed job queues for durable background work that needs priority ordering, batch claiming, worker recovery, retries, and progress visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may make an agent apply the skill to unrelated mentions of jobs, queues, or priorities.

Mitigation: Use it only for PostgreSQL-backed queue design tasks and confirm relevance before applying its guidance.

Risk: Generated queue schemas and worker code can affect production data processing if applied without review.

Mitigation: Review, test, and adapt the SQL and implementation guidance before deploying it to a live database.

## Reference(s):


## Skill Output:

**Output Type(s):** [markdown, code, configuration, guidance]

**Output Format:** [Markdown with SQL, PL/pgSQL, and Go code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
