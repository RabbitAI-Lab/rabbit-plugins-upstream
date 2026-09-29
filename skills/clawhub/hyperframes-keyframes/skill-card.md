## Description:

Guides authors in creating seek-safe 2D and 3D keyframe motion for HyperFrames compositions and verifying visible states with diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and developers use this skill to author seek-safe zooms, reframes, masks, paths, text motion, and depth effects in HyperFrames compositions, then check that key poses and final frames render as intended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's examples repeatedly run an unpinned npm executable, which may execute code that has not been reviewed.

Mitigation: Review the HyperFrames CLI source and provenance, use a controlled project, and prefer a locally installed lockfile-pinned binary or an exact reviewed package version, particularly in CI or repositories with secrets.

## Reference(s):

- [HyperFrames Keyframes on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-keyframes)
- [Keyframe Mechanism Reference](references/keyframe-patterns.md)
- [MDN CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes guidance for checking rendered keyframes and final states.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
