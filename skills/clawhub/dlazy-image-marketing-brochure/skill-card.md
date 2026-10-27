## Description:

A complete workflow skill for marketing brochure design, covering requirements gathering, layout design, and mock-up delivery through a layout-first process with a mandatory confirmation gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, designers, and businesses use this skill to plan promotional brochures and create layouts and mock-ups. It guides requirements gathering, fold and panel planning, image-generation prompts, and review checkpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference assets may be sent to dLazy's cloud image service.

Mitigation: Share only content approved for external processing; omit confidential or personal information.

Risk: API credentials may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Restrict access to saved credentials and revoke them when no longer needed.

Risk: The documentation contains an outdated CLI version reference.

Mitigation: Confirm the intended @dlazy/cli version against authoritative release information before installing or invoking it.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images]

**Output Format:** [Markdown design briefs and image-generation prompts; generated brochure layouts and mock-up images or URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a cloud image-generation service; mock-up production follows confirmation of the layout.]

## Skill Version(s):

1.3.34 (source: target release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
