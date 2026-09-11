## Description:

Turns a completed and verified agent workflow into a reusable skill by extracting its gates, observable rules, evidence requirements, and stopping conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and skill authors use this skill after a successful session to preserve a repeatable method as a local skill. It focuses on turning proven work into reusable guidance with explicit gates, evidence, boundaries, and review steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared agent memory may contain private, stale, or unrelated material that could influence a generated skill.

Mitigation: Keep the shared memory area trusted and free of secrets or unrelated private content before using the skill.

Risk: Mutable local vault rules can guide new skill creation and may change the generated result.

Mitigation: Review the active vault rules and inspect generated skills before deployment or publication.

Risk: Generated skills can preserve incorrect or misleading guidance if the original workflow was not actually verified.

Mitigation: Apply the skill's gate that only completed, verified, repeatable workflows are eligible for skill creation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-skillify)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [规则卡](references/规则卡.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local skill structure and review guidance; generated skills should be reviewed before use or publication.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata; artifact frontmatter reports 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
