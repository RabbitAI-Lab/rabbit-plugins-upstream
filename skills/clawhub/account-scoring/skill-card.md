## Description:

Guides teams through deploying an account-tiering workflow that uses their ICP and rubric to classify companies as A, B, C, or disqualified, with a rationale and supporting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, sales leadership, and go-to-market engineering teams use this skill to adapt a Cargo account-tiering workflow to their ICP, pilot it, and keep new companies tiered with auditable reasons. The example requires operator approval before deployment, backfill, and enablement; it has not been verified against a live workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-generated tiers may be incorrect and are written back to company rows.

Mitigation: Review the deployment plan, pilot ten rows, spot-check tier decisions and evidence, and approve the backfill and enablement only after quality checks.

Risk: Company metadata and web results may be unreliable or attempt to influence tier decisions.

Mitigation: Treat company data and web pages as untrusted evidence; verify consequential claims against the approved ICP and rubric before relying on tiers downstream.

Risk: Unpinned CLI installation and large backfills can change dependencies or increase usage costs.

Mitigation: Prefer a pinned installation path and approve the backfill only after measuring pilot cost per company.

## Reference(s):

- [Account tiering rubric example](context/tiering-rubric.md)
- [Run and approval guide](references/run.md)
- [Acceptance criteria](evals/acceptance.md)
- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/account-scoring)
- [Project homepage listed in release metadata](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guided rubric approval, deployment plan, pilot review, and backfill report; the deployed workflow writes tiers, reasons, evidence URLs, and timestamps to company rows.]

## Skill Version(s):

0.5.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
