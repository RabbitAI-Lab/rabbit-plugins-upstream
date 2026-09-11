## Description:

Analyze reviews or public customer feedback across multiple sources and produce themes, sentiment signals, and product actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn public customer reviews into evidence-backed themes, sentiment signals, source limitations, and prioritized product actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs access to a Dataify API token and can initiate paid Dataify collection requests.

Mitigation: Configure the token only through the local environment, never paste or print it in chat, keep source URLs explicit, use dry-run or max-actions for cost control, and monitor credit usage.

Risk: Resume files and local run state may affect what the skill reads or continues.

Mitigation: Resume only from state files you created and trust, keep output directories scoped to the intended run, and preserve task IDs instead of resubmitting paid tasks after timeouts.

Risk: A Dataify token may need rotation if it was exposed in logs or query-string task requests.

Mitigation: Review local logs before sharing them and rotate the Dataify token if there is any chance it was logged.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-review-intelligence)
- [Dataify token setup reference](artifact/_dependencies/skills/dataify-task-operations/references/token-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON reports with evidence-linked records, metrics, limitations, and resume state when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN for live collection; dry-run and max-actions support cost control.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
