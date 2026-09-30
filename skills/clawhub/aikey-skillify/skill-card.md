## Description:

Turns a completed, verified workflow from the current session into a reusable local agent skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using an agent can preserve a method that has already produced a verified result as a reusable local skill, with clear conditions for when to use it and how to check its output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create reusable local skill files and memory.

Mitigation: Review configured memory and vault paths before use and inspect generated files before reusing them.

Risk: Broad natural-language triggers may start the workflow before intended.

Mitigation: Use explicit commands where possible and confirm that the work is completed and verified before creating a skill.

## Reference(s):

- [Skill rule card](references/规则卡.md)
- [ClawHub skill listing](https://clawhub.ai/iamzifei/skills/aikey-skillify)

## Skill Output:

**Output Type(s):** [Markdown, Configuration instructions, Files]

**Output Format:** [Local skill files in Markdown with optional reference materials and evaluation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local reusable skill only after checking that the method was completed, verified, and likely to recur; publication requires a separate explicit request.]

## Skill Version(s):

0.3.4 (source: ClawHub release metadata; bundled SKILL.md declares 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
