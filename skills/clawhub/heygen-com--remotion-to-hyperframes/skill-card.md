## Description:

Ports explicitly requested Remotion (React) compositions to HyperFrames HTML and guides agents through linting, translation, validation, and documenting gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill when they have an existing Remotion source project and need a one-way migration path to HyperFrames HTML. It helps identify unsupported React patterns, generate HyperFrames compositions, run visual evaluation, and record translation gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask an agent to run unpinned network-fetched HyperFrames CLI update commands that may execute changing code or update installed skills.

Mitigation: Decline the self-update step unless the package and version can be verified; run conversion in a sandboxed project and review generated files plus TRANSLATION_NOTES.md before using outputs.

Risk: Translated compositions can be visually incorrect when Remotion patterns do not map cleanly to HyperFrames' seek-driven model.

Mitigation: Run lint_source.py before translation, stop on blockers and use the runtime interop recommendation, then validate acceptable translations with the render diff workflow and SSIM thresholds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)
- [Remotion to HyperFrames API Map](artifact/references/api-map.md)
- [Eval: how to validate a translation end-to-end](artifact/references/eval.md)
- [When to bow out: the runtime interop pattern](artifact/references/escape-hatch.md)
- [Translation limitations](artifact/references/limitations.md)
- [HyperFrames runtime interop PR](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code blocks and generated HyperFrames project files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce index.html, compositions/*.html, TRANSLATION_NOTES.md, lint findings, render commands, and SSIM evaluation summaries.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
