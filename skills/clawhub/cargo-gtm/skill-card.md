## Description:

Helps B2B go-to-market teams research accounts, verify professional contacts, qualify leads, draft permission-based outreach, and coordinate CRM and campaign workflows on Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and revenue teams use this skill to build qualified B2B account and contact lists, assess buying signals, verify work contact details, and prepare outreach for an approved sequencer. It can also help coordinate CRM updates and audience activation within consent, suppression, and spending limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospect data may be shared across connected providers, CRM systems, or advertising audiences without an appropriate basis.

Mitigation: Confirm the documented audience basis, apply suppression and relevance checks, and obtain approval before enrichment, CRM sync, or audience upload.

Risk: Installing a floating version of the Cargo CLI can change operational behavior unexpectedly.

Mitigation: Pin and review a specific CLI version before operational use.

Risk: Downloaded outputs and signed download links can expose sensitive contact records; CSV fields can be unsafe when opened in a spreadsheet.

Mitigation: Restrict access to output files and links, prefer JSON for automated processing, and neutralize formula-like CSV values before spreadsheet use.

Risk: Paid enrichment and recurring workflows can incur unexpected costs or repeat contact attempts.

Mitigation: Use a small pilot and explicit spend and scheduling approvals; honor suppression lists and contact-frequency limits.

## Reference(s):

- [Cargo GTM release on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Cargo skills homepage (declared in skill metadata)](https://github.com/getcargohq/cargo-skills)
- [Acceptable use and contact safeguards](artifact/references/acceptable-use.md)
- [Cost discipline and approval gates](artifact/references/cost-discipline.md)
- [Contact verification guidance](artifact/references/contact-accuracy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance, outreach drafts, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide exports of prospect records as JSON or CSV; requires the Cargo CLI and connected providers for operational workflows.]

## Skill Version(s):

2.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
