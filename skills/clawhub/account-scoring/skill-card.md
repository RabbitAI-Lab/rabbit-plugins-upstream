## Description:

Guides teams through adapting and deploying scheduled account tiering against their ICP, with explanations and optional CRM updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

RevOps, sales leaders, and GTM engineers use this skill to adapt an account-tiering workflow to their ICP, pilot it, and keep new or stale company records scored. The worked example requires approval before deployment and does not tier accounts on its own.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted company data and retrieved pages may influence LLM tier judgments that are written to Cargo or optional CRM fields.

Mitigation: Validate or isolate untrusted inputs before writing judgments, check the rubric and cited evidence in a pilot, and read back a sample of updated records.

Risk: Backfilling and frequent rescoring can incur substantial LLM and search costs.

Mitigation: Keep the scheduled play disabled until the ten-row pilot establishes cost, then approve the backfill and rescoring interval.

Risk: Installing unpinned tooling can introduce unreviewed changes.

Mitigation: Review the project plan before deployment and pin installation tooling where possible.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/account-scoring)
- [Publisher-provided project homepage](https://github.com/getcargohq/gtm-skills)
- [Account tiering rubric](context/tiering-rubric.md)
- [Pilot and deployment guide](references/run.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance with code and shell commands; adapted TypeScript project resources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed account tiers include a rationale and evidence URL; deployment and CRM updates require operator approval.]

## Skill Version(s):

0.5.3 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
