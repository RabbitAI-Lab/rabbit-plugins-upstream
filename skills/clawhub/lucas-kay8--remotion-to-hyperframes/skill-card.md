## Description:

Translates explicitly requested Remotion video compositions into HyperFrames HTML and GSAP compositions, while flagging unsupported patterns that should use runtime interop instead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lucas-kay8](https://clawhub.ai/user/lucas-kay8)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they need an agent to migrate an existing Remotion project into a HyperFrames composition and validate visual fidelity. The skill is intended for explicit migration requests, not for new HyperFrames authoring or casual Remotion references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The validation path can run mutable npm packages and rendering tools on the user's machine.

Mitigation: Run npm and render steps in a clean sandbox or container without unrelated credentials, and prefer pinned dependencies with lockfiles.

Risk: Generated HTML may include external script URLs or translated media references before rendering or publication.

Mitigation: Review generated HTML and asset references before rendering or publishing the output.

## Reference(s):

- [Remotion to HyperFrames API Map](artifact/references/api-map.md)
- [Runtime Interop Escape Hatch](artifact/references/escape-hatch.md)
- [Evaluation Guide](artifact/references/eval.md)
- [Translation Limitations](artifact/references/limitations.md)
- [Parameter Translation](artifact/references/parameters.md)
- [Sequencing Translation](artifact/references/sequencing.md)
- [Timing Translation](artifact/references/timing.md)
- [Media Translation](artifact/references/media.md)
- [Transitions Translation](artifact/references/transitions.md)
- [Lottie Translation](artifact/references/lottie.md)
- [Font Translation](artifact/references/fonts.md)
- [HyperFrames Runtime Interop PR #214](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, TypeScript, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce an index.html HyperFrames composition, validation commands, and translation notes depending on source complexity.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
