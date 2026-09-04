## Description:

Run lead discovery and outreach through Bavlio, the AI SDR that researches every lead before it writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bavlio](https://clawhub.ai/user/bavlio)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and growth teams use this skill to plan lead searches, enrich datasets, create outreach campaigns, and manage LinkedIn plus email replies through a Bavlio workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent receives access to Bavlio workspace data, including lead data, inbox context, credits, and outreach workflows.

Mitigation: Install only when that workspace access is acceptable for the intended agent and user.

Risk: Lead searches, enrichment, and campaign actions can spend Bavlio credits.

Mitigation: Review the search plan and maximum credit charge, then require explicit user approval before paid operations.

Risk: Campaign launches can send or schedule outbound LinkedIn and email outreach.

Mitigation: Review audiences, message copy, and final sequences before approving any campaign launch.

## Reference(s):

- [Bavlio ClawHub skill page](https://clawhub.ai/bavlio/skills/bavlio)
- [Bavlio documentation](https://bavlio.com/docs)
- [Bavlio website](https://bavlio.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Bavlio API key and user confirmation before paid searches or campaign launches.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
