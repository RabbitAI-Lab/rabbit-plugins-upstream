## Description:

Ports explicit Remotion React video compositions to HyperFrames HTML and guides validation of the translated output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they explicitly need to migrate an existing Remotion composition into a HyperFrames HTML composition, including linting, translation planning, generated output, and SSIM-based validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can install or run project dependencies, call local CLI tools, render videos, copy assets, and write generated output.

Mitigation: Run it only on trusted Remotion source or inside a sandbox, and review proposed commands and generated files before relying on the translation.

Risk: The optional skill update command can change installed skill content before use.

Mitigation: Approve the update only after considering whether refreshed skill content is acceptable for the current workspace.

Risk: Some Remotion patterns do not translate reliably to HyperFrames' seek-driven HTML model.

Mitigation: Run the bundled lint first, stop on blockers, use the documented runtime interop recommendation when needed, and validate completed translations with the SSIM evaluation workflow.

## Reference(s):

- [Remotion to HyperFrames skill page](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)
- [Remotion to HyperFrames API Map](references/api-map.md)
- [Evaluation Guide](references/eval.md)
- [Runtime Interop Pattern](references/escape-hatch.md)
- [Translation Limitations](references/limitations.md)
- [Timing Translation](references/timing.md)
- [Sequencing Translation](references/sequencing.md)
- [Media Translation](references/media.md)
- [Parameter Translation](references/parameters.md)
- [Transitions Translation](references/transitions.md)
- [HyperFrames Remotion Runtime Interop PR](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, TypeScript, JSON, and bash code blocks; generated HyperFrames files such as index.html and TRANSLATION_NOTES.md.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run lint, render, frame-diff, and frame-strip scripts and produce local validation artifacts.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
