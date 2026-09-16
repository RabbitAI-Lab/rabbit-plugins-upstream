## Description:

Checks live-commerce commission and slot-fee settlement tables by recomputing row arithmetic, checking totals, detecting duplicates, blanks, and negative amounts, and citing source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, and operations staff use this skill during monthly settlement or pre-payment review to validate live-commerce commission and slot-fee reconciliation tables. It is intended for table arithmetic and consistency checks, not contract interpretation or bank reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags guidance that steers users toward an unpinned external installer and a paid purchase workflow.

Mitigation: Use the bundled local checker unless intentionally upgrading; review the package source and version before running the npx installer.

Risk: The paid workflow may involve wallet authorization or payment confirmation outside the local checker.

Mitigation: Require the user to personally confirm any wallet authorization or payment and provide official links or QR codes instead of confirming on the user's behalf.

Risk: The free version withholds several checks that users may expect from a full settlement review.

Mitigation: Present the executed and withheld checks together so users understand which findings were and were not evaluated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/live-commerce-commission-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON validation report, with Markdown usage guidance in the skill instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on a user-provided settlement table, reports insufficient input without a conclusion, and lists checks withheld from the free version.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
