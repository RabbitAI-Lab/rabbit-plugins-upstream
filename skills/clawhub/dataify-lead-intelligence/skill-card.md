## Description:

Discover and rank companies that match an ideal customer profile using public company, hiring, and market evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and market research teams use this skill to build evidence-backed company prospect lists, qualify target accounts, and identify records that need human verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ICP details, keywords, geography, and source URLs are sent to Dataify when the workflow executes.

Mitigation: Use the skill only with inputs appropriate for Dataify processing under the configured API token and credits.

Risk: The workflow is not intended for private personal contact enrichment.

Mitigation: Limit use to organization-level public evidence and avoid requests for private personal emails, phone numbers, or individual contact enrichment.

Risk: Large or ambiguous scopes can consume credits or collect broader evidence than intended.

Mitigation: Use dry-run, bounded modes, max-action limits, and explicit geography or source URLs before larger jobs.

Risk: Untrusted resume state files can alter collection scope.

Mitigation: Resume only from state files created by the current user or otherwise trusted.

Risk: Automated qualification signals can be incomplete or misleading.

Mitigation: Review source evidence, missing fields, disqualifiers, and verification queues before using results for commercial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-lead-intelligence)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON reports and evidence file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces report.md, report.json, state.json, and raw evidence files in a bounded local run directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
