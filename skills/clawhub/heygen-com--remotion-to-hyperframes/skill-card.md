## Description:

Ports explicitly requested Remotion (React) composition source to HyperFrames HTML as a one-way Remotion-to-HyperFrames migration workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to translate existing Remotion video compositions into HyperFrames HTML, validate translation fidelity, and document unsupported or lossy patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run a silent self-update command before use.

Mitigation: Require explicit approval and review the exact npx hyperframes skills update remotion-to-hyperframes command before running it.

Risk: Translation and evaluation workflows can install npm packages, render media, write generated outputs, and run local shell scripts.

Mitigation: Run the workflow in an isolated checkout or container, and review generated files and commands before execution.

Risk: Unsupported Remotion patterns can produce misleading translations if they are ignored.

Mitigation: Run scripts/lint_source.py before translation, stop on blocker findings, use the runtime interop pattern when needed, and validate output with SSIM evaluation before relying on it.

## Reference(s):

- [Remotion to HyperFrames API Map](artifact/references/api-map.md)
- [Evaluation Guide](artifact/references/eval.md)
- [Escape Hatch and Runtime Interop](artifact/references/escape-hatch.md)
- [Translation Limitations](artifact/references/limitations.md)
- [Timing Translation](artifact/references/timing.md)
- [Media Translation](artifact/references/media.md)
- [HyperFrames Remotion Runtime Interop PR](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [Code, Files, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [HTML, Markdown notes, JSON lint and evaluation summaries, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce index.html, TRANSLATION_NOTES.md, copied media assets, SSIM summaries, and frame-diff artifacts when evaluation runs.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
