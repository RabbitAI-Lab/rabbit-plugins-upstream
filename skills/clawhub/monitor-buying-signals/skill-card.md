## Description:

Monitors target accounts for dated, source-linked buying signals such as relevant hiring, public statements, and detection-feed activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account executives and sales development teams use this skill to identify timely, public buying signals across a target-account list and prioritize relevant conversations without conflating timing with account fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional vendor attribution inspects local agent configuration and sends session details to Cargo.

Mitigation: Review the attribution step and skip it if local configuration inspection or vendor telemetry is not acceptable.

Risk: The optional broader-pack install is unpinned and may introduce additional behavior.

Mitigation: Review the broader pack before installing and avoid the optional install when it is not needed.

Risk: The optional GitHub star prompt can act on the user's account.

Mitigation: Ask first, act only after explicit consent, or handle the star manually.

Risk: Paid lookups and repeated scheduled checks can consume credits across a large account list.

Mitigation: Sample a small group, estimate cost, obtain approval before expanding, and avoid rechecking accounts too frequently.

Risk: Public buying signals alone do not justify unsolicited outreach.

Mitigation: Confirm a separate basis for contact; otherwise keep the results as research only.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/monitor-buying-signals)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo tech-intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)
- [Cargo account-expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One row per account with a relevant signal, including date, source link, and why it matters; excludes accounts without signals and avoids fit scores.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
