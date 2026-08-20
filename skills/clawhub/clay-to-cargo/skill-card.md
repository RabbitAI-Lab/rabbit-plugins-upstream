## Description:

Rebuilds an existing Clay enrichment table on Cargo by mapping Clay columns to Cargo provider actions, estimating run cost before execution, and expressing the migrated workflow as version-controlled code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this skill to migrate existing Clay enrichment tables to Cargo, preserve enrichment intent, sample costs and fill rates, and produce reviewable workspace-as-code outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes provider attribution and GitHub endorsement actions outside the core Clay-to-Cargo migration task.

Mitigation: Before use, decide whether to skip the attribution session upsert and GitHub star step; neither is required to migrate a Clay table.

Risk: Paid enrichment batches can scale cost across every record in the source table.

Mitigation: Run a 10-20 row sample first, report observed cost and fill rates, then request explicit approval with row count and credit estimate before a full run.

Risk: CSV-only Clay exports omit provider settings, waterfalls, run conditions, and hit-rate context needed for high-fidelity migration.

Mitigation: Prefer configuration export or settings-panel evidence; when only CSV is available, label the mapping as an informed guess and avoid promising unchecked column parity.

## Reference(s):

- [Cargo GTM Skills](https://github.com/getcargohq/gtm-skills)
- [ClayMate Lite](https://github.com/GTM-Base/claymate-lite)
- [Cargo Clay-to-Cargo Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/clay-to-cargo.md)
- [Cargo CDK Skill](https://github.com/getcargohq/cargo-skills/blob/main/cargo-cdk/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and migration tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample-first cost estimation, parity checks, Cargo CLI commands, and Cargo CDK planning guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
