## Description:

Helps developers port existing Remotion video compositions into HyperFrames HTML and validate the visual result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers migrating an existing Remotion composition use this skill to map compatible animation and media patterns to HyperFrames, generate HTML compositions, and compare renders. Unsupported React patterns are flagged rather than silently translated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup, catalog searches, rendering, and fonts or CDN assets may contact external services or fetch dependencies.

Mitigation: Review and approve npx/npm install, update, add, render, and external-asset steps before running them, especially in private or restricted projects.

Risk: Some Remotion behavior cannot be translated faithfully into HyperFrames.

Mitigation: Lint the source for blockers, document dropped or approximated features, and compare rendered frames before accepting the conversion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)
- [Remotion API mapping](references/api-map.md)
- [Translation evaluation guide](references/eval.md)
- [Translation limitations](references/limitations.md)
- [HyperFrames runtime interop proposal](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [HTML compositions and Markdown translation notes with shell commands for validation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include lint findings and render-difference results.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
