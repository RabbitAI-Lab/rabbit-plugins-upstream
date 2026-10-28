## Description:

Use GISDB to inspect available county property records, ask relevant search questions, save and resume private searches, and manage explicitly requested reviewed-offer checkout and lead subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

Property researchers and real-estate professionals use GISDB to inspect county property records, save and resume searches, and manage explicitly requested lead purchases and subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake pausing lead updates for stopping recurring billing.

Mitigation: Explain that pausing updates does not cancel billing; use the requested cancellation flow and confirm the order status.

Risk: Users may commit to a purchase without understanding its price or terms, or mistake a checkout return for confirmed payment.

Mitigation: Review the exact price, coverage, billing interval, source-check cadence, and limitations before checkout; verify payment and delivery through the returned order status. Keep payment details on the hosted checkout page.

## Reference(s):

- [GISDB integration and release notes](https://gisdb.io/integrations/0.4.1)
- [Research and package selection](artifact/references/research-and-packages.md)
- [Commerce and recovery](artifact/references/commerce-and-recovery.md)
- [Untax separate connection](https://untax.io/integrations/0.4.1#quick-start)
- [GISDB ClawHub release page](https://clawhub.ai/mooshee/skills/gisdb)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Text guidance and structured JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports returned coverage, dates, recorded facts, limitations, offers, and order status; unknown facts remain unknown.]

## Skill Version(s):

0.4.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
