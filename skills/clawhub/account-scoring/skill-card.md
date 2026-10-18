## Description:

Guides deployment of scheduled account tiering against an approved ICP rubric, with reasons and evidence written to Cargo and optional HubSpot or Salesforce company records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, sales leaders and go-to-market engineers use this skill to configure, pilot and deploy recurring account tiers with auditable reasons and optional CRM writeback. The example is not yet verified against a live workspace and requires operator approval before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted company fields may influence tiering and be persisted to Cargo or CRM records.

Mitigation: Separate company data from trusted instructions, gate persistence on evaluator success, and review pilot results before enabling writes.

Risk: Deployment or backfill may write incorrect tiers at scale or update CRM fields unexpectedly.

Mitigation: Keep CRM writeback disabled until approved, review the deployment plan, pilot a small batch and confirm CRM records before backfill or enabling the play.

Risk: Unreviewed installation commands or dependencies may introduce unwanted code.

Mitigation: Review and pin installation commands and verify the cargo-cdk dependency source before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/account-scoring)
- [Declared project homepage](https://github.com/getcargohq/gtm-skills)
- [Run guide](references/run.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance with code and command examples; deployed agent writes structured tier, rationale, evidence URL and timestamp to account records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four account tiers (A, B, C, disqualified); optional CRM writeback after approval]

## Skill Version(s):

0.5.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
