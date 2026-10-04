## Description:

Guides the one-way translation of existing Remotion compositions into HyperFrames HTML compositions, with checks for unsupported patterns and render fidelity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers migrating an existing Remotion video composition to HyperFrames use this skill to translate scenes, timing, media, and animation into HTML and identify gaps that need review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local lint, render, and diff commands run on project files, including projects with untrusted dependencies.

Mitigation: Use only with Remotion projects you trust and review commands before running them.

Risk: CLI installation or skill updates can bring in changing external tooling.

Mitigation: Prefer pinned or project-local CLI versions and confirm skill updates or catalog additions.

Risk: Translated animations or assets may differ from the source.

Mitigation: Compare renders and review translation notes before using the result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)
- [HyperFrames Remotion interoperability pattern](https://github.com/heygen-com/hyperframes/pull/214)
- [HyperFrames and Remotion guide](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/hyperframes-vs-remotion.mdx)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands]

**Output Format:** [HTML composition files, translation notes in Markdown, and validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assets and a visual comparison report; unsupported patterns are flagged rather than translated.]

## Skill Version(s):

1.0.14 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
