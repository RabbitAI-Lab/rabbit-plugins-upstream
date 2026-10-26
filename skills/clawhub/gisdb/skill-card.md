## Description:

Use GISDB to inspect available county property records, ask relevant search questions, save and resume private searches, and manage explicitly requested reviewed-offer checkout and lead subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

External users can research available county property records, save and resume private searches, and manage explicitly requested purchases or lead subscriptions through GISDB.

### Deployment Geography for Use:

United States (supported county coverage varies; check the current GISDB catalog).

## Known Risks and Mitigations:

Risk: GISDB receives search inputs and stores searches the user chooses to save.

Mitigation: Review account permissions and purchase terms, and save searches only when desired.

Risk: Recurring plans can continue billing while updates are paused.

Mitigation: Use subscription cancellation to stop renewal; pausing updates alone does not stop billing.

## Reference(s):

- [GISDB integrations and release notes](https://gisdb.io/integrations/0.4.1)
- [Research and package selection](artifact/references/research-and-packages.md)
- [Commerce and recovery](artifact/references/commerce-and-recovery.md)
- [Untax separate connection guide](https://untax.io/integrations/0.4.1#quick-start)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Conversational summaries and structured JSON results when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on supported county coverage and available records; missing facts remain unknown.]

## Skill Version(s):

0.4.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
