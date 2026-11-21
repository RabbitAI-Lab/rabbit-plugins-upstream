## Description:

Reviews AI-generated ecommerce images for visual and platform risks, then returns a risk rating, itemized checks, a release recommendation, and prompt-ready corrections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and reviewers use this skill to inspect AI-generated product images before listing or advertising and identify needed corrections or reruns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags a mismatch between the stated purpose and some implemented behavior, and notes incomplete analysis.

Mitigation: Review the skill’s checks and reports against your image-quality requirements before relying on it.

Risk: A read-error handling weakness could leave an image unchecked.

Mitigation: Treat unreadable images as unresolved and verify that each image was actually inspected before acting on a successful status.

Risk: Images may be sent to external AI providers during review.

Mitigation: Confirm that external processing is acceptable for the images in your workflow before submitting them.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/detect-task)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Chinese Markdown report with a risk rating, eight itemized checks, a listing recommendation, and English prompt corrections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May review up to 10 images per call; can provide prompt-ready corrections for reruns.]

## Skill Version(s):

1.0.35 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
