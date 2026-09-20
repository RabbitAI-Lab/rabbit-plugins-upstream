## Description:

Ports explicit Remotion (React) composition source into one-way HyperFrames HTML translations with validation guidance and escape-hatch recommendations for unsupported patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video tooling engineers use this skill to migrate existing Remotion compositions to HyperFrames HTML and GSAP, lint unsupported React patterns, validate render fidelity with SSIM checks, and document translation gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to update installed skills and run unpinned npm or npx tooling that can change behavior or execute code on the user's machine.

Mitigation: Review before installing, confirm skill updates explicitly, use a project sandbox, and prefer locked or local HyperFrames and Remotion CLI versions.

Risk: The evaluation harness can run npm installs, render tooling, and generated output writes in the active workspace.

Mitigation: Run the harness only in disposable or non-sensitive project copies after reviewing the scripts and expected output paths.

## Reference(s):

- [Remotion to HyperFrames API Map](artifact/references/api-map.md)
- [Runtime Interop Escape Hatch](artifact/references/escape-hatch.md)
- [Translation Evaluation Guide](artifact/references/eval.md)
- [Translation Limitations](artifact/references/limitations.md)
- [Timing Translation](artifact/references/timing.md)
- [Sequencing Translation](artifact/references/sequencing.md)
- [Media Translation](artifact/references/media.md)
- [Parameter Translation](artifact/references/parameters.md)
- [Transition Translation](artifact/references/transitions.md)
- [Font Translation](artifact/references/fonts.md)
- [Lottie Translation](artifact/references/lottie.md)
- [HyperFrames Remotion Runtime Interop PR](https://github.com/heygen-com/hyperframes/pull/214)
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline commands, generated HTML/GSAP code, configuration notes, and JSON lint or evaluation summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce HyperFrames source files, TRANSLATION_NOTES.md, SSIM summary JSON, and visual diff artifacts during validation.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
