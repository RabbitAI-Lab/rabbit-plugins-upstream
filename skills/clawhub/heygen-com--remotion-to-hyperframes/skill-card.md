## Description:

Helps developers migrate an existing Remotion composition into HyperFrames HTML and validate the translated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to port existing Remotion source into HyperFrames compositions, compare renders, and document translation gaps. It does not support reverse conversion or unrelated animation sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: npm/npx installs, updates, and renders carry developer-tool supply-chain risk.

Mitigation: Review commands before approval and prefer pinned or project-local package versions in sensitive environments.

Risk: Unsupported React patterns or lossy translations can produce incorrect video output.

Mitigation: Lint source first, decline blocked translations, compare renders, and document any remaining gaps.

## Reference(s):

- [Remotion to HyperFrames API map](artifact/references/api-map.md)
- [Evaluation and render comparison](artifact/references/eval.md)
- [Translation limitations](artifact/references/limitations.md)
- [Runtime interop for unsupported compositions](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Guidance]

**Output Format:** [HyperFrames HTML and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include translation notes and render-comparison guidance; unsupported inputs receive an interop recommendation.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
