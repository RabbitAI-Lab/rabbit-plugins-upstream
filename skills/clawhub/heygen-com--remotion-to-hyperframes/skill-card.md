## Description:

Ports an existing Remotion (React) composition source to HyperFrames HTML for explicit one-way Remotion-to-HyperFrames migration requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to translate existing Remotion video compositions into HyperFrames HTML, GSAP timelines, validation commands, and migration notes. It is intended for explicit Remotion source migration requests and declines reverse or non-Remotion conversions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a silent self-update step before use.

Mitigation: Review or remove the self-update behavior before installation and pin the skill version used in production workflows.

Risk: The workflow runs local package and rendering commands against user-provided Remotion projects.

Mitigation: Run it in a disposable workspace or container, avoid untrusted projects, and pin package versions before executing render or diff commands.

Risk: Generated output may depend on external CDN scripts.

Mitigation: Vendor scripts locally or add integrity pinning for production releases.

## Reference(s):

- [Remotion to HyperFrames skill](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)
- [Remotion to HyperFrames API Map](artifact/references/api-map.md)
- [Eval: how to validate a translation end-to-end](artifact/references/eval.md)
- [When to bow out: the runtime interop pattern](artifact/references/escape-hatch.md)
- [Translation limitations](artifact/references/limitations.md)
- [Runtime interop pattern PR](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated HTML, CSS, JavaScript, shell command snippets, and optional translation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce index.html and TRANSLATION_NOTES.md for translated compositions; recommends runtime interop instead of translation when blocker patterns are detected.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
