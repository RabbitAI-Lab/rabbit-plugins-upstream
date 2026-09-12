## Description:

Ports an explicitly provided Remotion React composition source into one-way HyperFrames HTML output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they need to migrate an existing Remotion composition into a HyperFrames HTML and GSAP composition, including linting unsupported Remotion patterns and validating visual fidelity with render comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable update and package or render commands may change installed skill instructions or pull unpinned code before use.

Mitigation: Review and approve update/render commands, pin the HyperFrames CLI where practical, and run npm or render work in a sandbox without secrets.

Risk: The bundled test corpus and render flow may rely on dependencies or CDN assets that are not locked or vendored.

Mitigation: Avoid or isolate the bundled test corpus until dependencies and CDN assets are reviewed, locked, or vendored.

Risk: Unsupported Remotion patterns can produce incorrect HyperFrames translations if they are forced through the conversion workflow.

Mitigation: Run the provided lint step first, stop on blocker findings, use the documented runtime interop pattern for blockers, and validate translations with the SSIM render-diff workflow.

## Reference(s):

- [Remotion to HyperFrames API Map](references/api-map.md)
- [Escape Hatch and Runtime Interop Pattern](references/escape-hatch.md)
- [Translation Evaluation Guide](references/eval.md)
- [Translation Limitations](references/limitations.md)
- [Parameter Translation](references/parameters.md)
- [Sequencing Translation](references/sequencing.md)
- [Timing Translation](references/timing.md)
- [Media Translation](references/media.md)
- [Transition Translation](references/transitions.md)
- [Lottie Translation](references/lottie.md)
- [Font Translation](references/fonts.md)
- [HyperFrames Runtime Interop PR #214](https://github.com/heygen-com/hyperframes/pull/214)
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated HTML, CSS, JavaScript, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate HyperFrames index.html output, TRANSLATION_NOTES.md, lint findings, and render-diff validation summaries.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
