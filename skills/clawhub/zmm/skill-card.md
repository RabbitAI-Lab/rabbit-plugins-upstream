## Description:

詹明明 is a zmm-family entry-point skill that helps an agent onboard users, route content or business tasks to the right zmm skill, and return a ready-to-send prompt for the selected next tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill as the public entry point for the zmm tool family: it routes short-form content workflows, script review and retrospectives, and small-business diagnostic requests to one primary zmm skill with optional supporting skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases can route an ordinary request into the zmm workflow.

Mitigation: Confirm the task area and selected zmm skill before sending or running the generated prompt.

Risk: Full zmm workflows may use configured account files, local paths, or skill memory.

Mitigation: Review zmm configuration and omit sensitive local paths or account data unless that sharing is intended.

Risk: The router may recommend downstream skills that produce files or update memory as part of their own workflows.

Mitigation: Run only the selected downstream skills needed for the current task and review their prompts before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm)
- [交互规范](artifact/references/交互规范.md)
- [内容理论底座](artifact/references/内容理论底座.md)
- [实证规律库](artifact/references/实证规律库.md)
- [zmm 技能家族公约](artifact/references/家族公约.md)
- [认知框架](artifact/references/认知框架.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with ready-to-send prompt blocks and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend one primary zmm skill and up to two supporting zmm skills; it normally stops after generating the next prompt.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
