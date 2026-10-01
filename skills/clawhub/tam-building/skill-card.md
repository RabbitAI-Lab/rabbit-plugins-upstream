## Description:

Helps revenue operations and sales teams build a company universe, size sourcing costs, and assign evidence-backed account tiers using their own ICP and rubric.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, go-to-market engineers, and sales leaders use this skill to adapt a Cargo pipeline that sources companies matching their ICP, tiers each account against a workspace rubric, and records reasons and evidence for sales prioritization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted company text can influence LLM-generated account rankings that are saved in the workspace.

Mitigation: Clearly separate company fields from instructions and require a passing evaluator result before writing tier columns.

Risk: Sourcing can incur per-record charges or create unwanted changes in a live workspace.

Mitigation: First test in a separate Cargo workspace, review the plan and costs, and keep the play disabled until approved.

Risk: Example ICP and tiering criteria may produce inappropriate account judgments.

Mitigation: Replace the example ICP and rubric, especially the language criterion, with reviewed business rules and pin CLI and cargo-cdk skill versions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/tam-building)
- [Publisher project homepage (listed in release metadata; import provenance unavailable)](https://github.com/getcargohq/gtm-skills)
- [Configuration guide](references/configure.md)
- [Run guide](references/run.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with code and shell commands; adapted Cargo project resources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The deployed pipeline records account tier, rationale, evidence URL, and tiering timestamp.]

## Skill Version(s):

0.3.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
