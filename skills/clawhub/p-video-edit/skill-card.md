## Description:

p-video-edit helps agents edit an existing short video from a text instruction, such as changing colors, lighting, environments, on-screen text, or objects while preserving unrequested elements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to prepare prompt-driven edits for existing videos through Pruna's API. It is intended for targeted changes such as attributes, environment, relighting, text, object edits, or reference-guided product and accessory edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided videos and optional reference images are uploaded to Pruna's cloud API.

Mitigation: Do not upload confidential or restricted media unless Pruna's data handling terms meet the user's needs.

Risk: A broad or ambiguous edit prompt can change unrequested parts of the source clip.

Mitigation: Use a single principal change, explicit preserve clauses, and review the prompt before submitting the API request.

Risk: Prediction calls can incur per-second billing for returned video output.

Mitigation: Confirm the source video, prompt, draft setting, and edit intent before paid API calls; use draft mode for lower-cost previews when appropriate.

## Reference(s):

- [ClawHub skill page: p-video-edit](https://clawhub.ai/pruna-ai/skills/p-video-edit)
- [Pruna files API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY; source videos are limited to 15 seconds; optional reference images are limited to 4 files.]

## Skill Version(s):

1.0.13 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
