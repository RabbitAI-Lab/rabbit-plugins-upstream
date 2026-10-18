## Description:

Guides teams through auditing and deduplicating CRM accounts and contacts, merging high-confidence matches and routing uncertain matches for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and CRM engineering teams use this skill to audit duplicate accounts or contacts, configure matching and survivor policies, and pilot recurring CRM merges with approval for uncertain cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic or approved merges can alter live CRM records.

Mitigation: Approve each path's matching and survivor policy, then pilot with plays disabled and capped before enabling merges.

Risk: A mistaken CRM or review-channel configuration can affect the wrong records or send review requests to the wrong audience.

Mitigation: Verify the CRM connector, record fields, Slack destination, and exact pilot population before deployment.

Risk: Installing an unpinned CLI can introduce supply-chain changes.

Mitigation: Review or pin the CLI installation path when supply-chain control is required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/crm-deduplication)
- [Project homepage (declared in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Audit guide](references/audit.md)
- [Configuration guide](references/configure.md)
- [Run guide](references/run.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands, Markdown]

**Output Format:** [Markdown instructions and project code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separate account and contact paths with independent approval and pilot checks.]

## Skill Version(s):

0.1.2 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
