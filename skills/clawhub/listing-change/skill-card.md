## Description:

Monitors saved Amazon listing snapshots and reports deterministic diffs for titles, bullets, images, and related page fields on supported schedules; it does not perform hourly monitoring, call paid LLMs, modify listings, or infer sales, inventory, orders, or return rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and developers use this skill to manage ARI listing-change watches for ASINs, review recent snapshot-diff digests, and pause, resume, or delete watch records after considering daily or weekly scan costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the user to authorize or provide an ARI API key and stores that key locally.

Mitigation: Install and configure it only for users who intend to connect an ARI account, and use the setup or configure flow rather than embedding keys in prompts or files.

Risk: Creating or changing watches can affect daily or weekly scan costs and account quotas.

Mitigation: Review the daily or weekly scan cost and available quota before creating or modifying a watch, and perform management actions only after explicit user direction.

Risk: The watch workflow may be unavailable if the packaged CLI does not expose the required watch subcommands.

Mitigation: Run the watch help check before use and stop with an upgrade prompt if the required watch commands are unavailable.

## Reference(s):

- [ClawHub listing-change skill page](https://clawhub.ai/funewa/skills/listing-change)
- [Amazon Listing Change Alert reference](references/reference.md)
- [Amazon Listing Change Alert watch workflow](references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands and ARI watch summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses the fixed watch/listing workflow with watch_digest output.]

## Skill Version(s):

1.4.13 (source: server release metadata and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
