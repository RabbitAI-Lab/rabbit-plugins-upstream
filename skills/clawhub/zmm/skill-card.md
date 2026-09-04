## Description:

詹明明 is the entry router for the zmm skill family, guiding users to content-production or small-business decision skills through onboarding, pre-task routing, and post-task navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and small-business operators use this skill to choose the right zmm downstream skill, get a ready-to-send prompt, or decide the next step after a zmm skill produces a result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The router may run local discovery and inspect downstream zmm skill instructions before producing a prompt.

Mitigation: Review installed downstream zmm skills and the local config/vault setup before using the routed prompt.

Risk: Downstream skills may read local content workspace files or write drafts and memory records.

Mitigation: Confirm workspace paths, configuration, and downstream skill permissions before executing the selected skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iamzifei/skills/zmm)
- [zmm 技能家族公约](references/家族公约.md)
- [交互规范](references/交互规范.md)
- [内容理论底座](references/内容理论底座.md)
- [认知框架](references/认知框架.md)
- [实证规律库](references/实证规律库.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, text, shell commands, configuration]

**Output Format:** [Markdown guidance with numbered choices and ready-to-send prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local configuration, vault paths, and a read-only discovery script when routing to installed zmm skills.]

## Skill Version(s):

0.2.3 (source: ClawHub release metadata; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
