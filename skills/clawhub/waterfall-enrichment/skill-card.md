## Description:

Helps agents enrich contact and company records through a prioritized sequence of data providers and verify resulting email addresses with Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and go-to-market teams use this skill to enrich batches of contact or company records across providers, verify email results, and estimate costs before larger runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospect or customer records are sent to Cargo and its enrichment providers.

Mitigation: Use only records authorized for sharing with Cargo and its providers; review applicable privacy requirements first.

Risk: Setup records skill-attribution information and checks a local Claude plugin configuration file.

Mitigation: Review the setup steps and local configuration access before running them.

Risk: Unpinned package installation can change the CLI used by the skill.

Mitigation: Review and pin an approved CLI version before installation.

Risk: The skill may propose starring a GitHub repository using the user's account.

Mitigation: Do not perform the account action without the user's explicit consent.

Risk: Large enrichment batches may incur substantial credits, and enriched addresses may be inaccurate.

Mitigation: Sample 10–20 records, report cost and match rate, obtain approval for the full batch, and verify email results.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo waterfall provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/waterfall.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with Cargo CLI commands and enrichment result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results can include matched contact or company details, email verification status, provider, hit rate, and estimated credits.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
