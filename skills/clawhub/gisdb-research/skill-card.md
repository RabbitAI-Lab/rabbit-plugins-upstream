## Description:

Use GISDB to inspect available county property records, ask relevant search questions, save and resume private searches, and manage explicitly requested reviewed-offer checkout and lead subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

External users researching county property records and lead packages can ask evidence-based questions, review source coverage and dates, and manage saved searches. The skill also supports user-requested purchases and lead update subscriptions with explicit review and order readback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pausing lead updates does not stop subscription renewal.

Mitigation: Check the order and billing status separately; use cancellation only when the user requests stopping renewal.

Risk: Account permissions and purchase terms affect private searches, checkout, and billing actions.

Mitigation: Review the connected GISDB account permissions and exact offer terms before carrying out a requested action; keep payment details on the hosted checkout page.

## Reference(s):

- [GISDB setup and release notes](https://gisdb.io/integrations/0.4.1)
- [Research and package selection](references/research-and-packages.md)
- [Commerce and recovery](references/commerce-and-recovery.md)
- [Untax separate connection guide](https://untax.io/integrations/0.4.1#quick-start)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Natural-language research summaries and guidance, with structured JSON results where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports source dates, coverage, recorded facts, and missing information; does not infer missing facts.]

## Skill Version(s):

0.4.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
