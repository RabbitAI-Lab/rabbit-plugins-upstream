## Description:

Builds an on-demand Cargo tool that finds, qualifies, ranks, and returns relevant stakeholders for supplied accounts, with optional verified work email and phone enrichment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development, RevOps, and GTM engineering teams use it to build a reusable workflow that ranks stakeholders by relevance to a seller's product at supplied accounts. Operators can request all qualified people or up to a chosen count, with optional work email or phone enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious because setup references an unpinned `npx skills` command, and 2 of 8 components were only partially inspected.

Mitigation: Pin the CLI and dependency to reviewed versions and resolve the incomplete scan before installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/contact-sourcing)
- [Project overview](artifact/README.md)
- [Installation and approval procedure](artifact/SKILL.md)
- [Seller research and criteria review](artifact/references/audit.md)
- [Configuration and output contract](artifact/references/configure.md)
- [Sample calibration and handoff](artifact/references/run.md)
- [Acceptance and validation status](artifact/evals/acceptance.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Guidance]

**Output Format:** [Cargo tool configuration, TypeScript code, and Markdown instructions]

**Output Parameters:** [Per supplied account; all qualified stakeholders or up to a chosen maximum]

**Other Properties Related to Output:** [Ranked contacts retain profile evidence and status. Verified work email and phone enrichment are optional and independent of the result limit.]

## Skill Version(s):

0.1.0 (source: artifact/SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
