## Description:

Helps teams deploy an agent that scores and tiers accounts against their written ICP and writes scores and rationales back to the CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, sales leadership, and GTM engineering teams use this skill to adapt and deploy ongoing account scoring, tiering, and CRM writeback against their ICP. The worked example requires workspace CRM and LLM connections and should be reviewed before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated scoring can overwrite CRM fields or propagate incorrect scores and rationales.

Mitigation: Test on a sandbox or small sample, use dedicated CRM fields, inspect the deployment plan, and require explicit approval before production writeback.

Risk: Manipulated account names or domains can influence model-produced CRM updates.

Mitigation: Validate or review unusual account data, large score changes, and model-produced rationales before enabling production writeback.

## Reference(s):

- [ClawHub account-scoring release](https://clawhub.ai/cargo-ai/skills/account-scoring)
- [Project homepage (release metadata)](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance with TypeScript examples and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Example deploys an account scorer that writes score, tier, rationale, and update time to CRM records.]

## Skill Version(s):

0.2.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
