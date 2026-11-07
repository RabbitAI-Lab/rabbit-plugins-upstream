## Description:

Generates text-to-video and image-to-video clips through PopNow, selecting a model, showing the exact USD quote, and creating the clip after approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agents use this skill to create short videos from text prompts or animate supplied images with PopNow-supported models. It checks current model schemas and prices, presents the maximum USD charge for approval, then creates and tracks the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video generation uses a paid prepaid API balance.

Mitigation: Use a dedicated API key with spending limits and approve the quoted maximum price before each generation.

Risk: Prompts and media URLs are shared with PopNow and the generation provider; command logs may retain inputs, and provider-side retention was not independently tested.

Mitigation: Submit only prompts and media you are comfortable sharing, and avoid sensitive personal data.

Risk: An exposed API key could be used to make requests against the account.

Mitigation: Keep the key in secret or environment settings, never in chat or command arguments, and restrict its models, IPs, and spending caps.

## Reference(s):

- [PopNow video generation](https://popnow.ai/video)
- [PopNow task API documentation](https://popnow.ai/docs/tasks)

## Skill Output:

**Output Type(s):** [Video, API Calls, Guidance]

**Output Format:** [Generated video output links with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available output and settings depend on the selected model and its schema.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
