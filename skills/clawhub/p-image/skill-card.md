## Description:

Use when someone explicitly wants the fastest, cheapest photo generation -- mood boards, bulk panels, or quick iterations -- not when controlled photoreal or in-image text is needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to route simple still-image requests to Pruna's p-image API, draft faithful prompts, confirm prompt and aspect ratio before generation, and produce curl commands for async or quick test calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Pruna API key for network image-generation requests.

Mitigation: Confirm PRUNA_API_KEY is configured only in the execution environment and avoid exposing it in prompts, logs, or shared command output.

Risk: Image-generation requests may consume paid or limited quota.

Mitigation: Show the drafted prompt and aspect ratio before making API calls unless the user has already locked the wording.

Risk: Simple image generation may be a poor fit for controlled photorealism, readable in-image text, edits, or video.

Mitigation: Route those requests to the more specific Pruna skills named by the artifact instead of re-running p-image.

## Reference(s):

- [ClawHub p-image release page](https://clawhub.ai/pruna-ai/skills/p-image)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY for API calls; image generation can consume paid quota.]

## Skill Version(s):

1.0.10 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
