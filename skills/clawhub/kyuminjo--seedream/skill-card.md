## Description:

Generate and edit images or split them into layers with ByteDance Seedream 5.0 models through PopNow, with exact USD quotes before paid generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate or edit images with Seedream 5.0, maintain subject consistency across reference images, and request layer decomposition through PopNow after reviewing the quoted cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media URLs are sent to PopNow and the generation providers.

Mitigation: Avoid sensitive material and only submit reference media the user has rights to use.

Risk: Image generation uses a paid API balance, and live billing and privacy practices were not independently verified.

Mitigation: Review the exact quoted maximum before each generation, use a dedicated key with model restrictions and spending caps, and consult PopNow's current billing and privacy terms.

## Reference(s):

- [Seedream 5.0 model page](https://popnow.ai/models/seedream-5-0-pro)
- [PopNow task API documentation](https://popnow.ai/docs/tasks)

## Skill Output:

**Output Type(s):** [Generated images, Image layer outputs, Output links, JSON task and quote results]

**Output Format:** [Image outputs returned as links, with JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Layer decomposition returns separate layer links rather than a single PSD file.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
