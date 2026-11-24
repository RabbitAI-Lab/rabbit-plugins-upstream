## Description:

Checks product images against marketplace listing rules and reports rejection risks, with automatic fixes for supported geometry and color issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce teams use this skill to check product images against marketplace listing specifications, review likely rejection causes, and correct supported image issues before upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The benign scan has medium confidence and partial coverage: 60% of components were covered, some files were only partly inspected, and several static analyzers were degraded.

Mitigation: Review the skill before installation and inspect its scripts for the workflows you plan to use.

Risk: Image-generation workflows can send prompts and local images to the selected cloud provider.

Mitigation: Use a provider whose data handling meets your requirements, and avoid sending sensitive images or prompts.

## Reference(s):

- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Related detect-task skill (visual content checks)](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Files, Guidance]

**Output Format:** [Plain-text or JSON compliance report; optionally corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marketplace rules are a machine-checkable subset; text, watermarks, and product defects require separate visual or manual review.]

## Skill Version(s):

1.0.34 (source: SKILL.md frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
