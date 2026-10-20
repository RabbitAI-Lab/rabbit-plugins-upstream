## Description:

Generates a set of clothing-model images with varied poses and viewing angles from one reference image for product pages and social media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use this skill to turn one clothing-model photo into a set of pose and angle variations for product listings and social media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or executing unpinned external tooling may change the local Node/npm environment.

Mitigation: Review and approve installation first; prefer a pinned qhkit version and avoid npx or @latest execution where possible.

Risk: Setup guidance can make persistent changes to shell configuration.

Mitigation: Keep PATH changes temporary unless the user explicitly wants them persisted.

Risk: Reference images and API tokens may be sent to the LinkPix/qhkit service.

Mitigation: Only upload images and provide tokens the user is comfortable sharing with the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-model-pose-set)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown guidance and JSON results with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports actual credit usage; generated garment details require visual review.]

## Skill Version(s):

0.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
