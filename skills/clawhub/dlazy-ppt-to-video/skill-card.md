## Description:

Converts PPT, PowerPoint, Keynote, and related document inputs into video workflows by helping parse the source, outline, storyboard, create voiceover, build, and validate an explainer or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, educators, and business users use this skill to turn presentations or other documents into explainer, pitch, courseware, report, or training video workflows through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and explicitly attached files may be sent to the external dLazy service.

Mitigation: Use the skill only when that data can be shared with dLazy, attach only intended files, and avoid sensitive non-presentation documents unless upload controls are clarified.

Risk: The skill name emphasizes PPT conversion, while the artifact behavior also covers broader document-to-video workflows.

Mitigation: Confirm the intended input scope before use and review outputs when converting non-presentation documents.

Risk: A global CLI install persists an executable in the user environment.

Mitigation: Prefer the pinned npx invocation or another isolated execution method, and verify the @dlazy/cli package or source before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI response text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded files, dLazy project ids, and follow-up CLI commands needed to continue a project.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
