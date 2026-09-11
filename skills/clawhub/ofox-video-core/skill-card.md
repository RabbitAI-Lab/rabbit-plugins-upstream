## Description:

Requires OFOX_API_KEY; provides a shared execution layer for creating, polling, downloading, and cost-reporting Ofox video generation jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this library skill to call the Ofox video API with low-level parameters, resume or debug video jobs by job id, and support scenario skills that generate video prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dotenv loading can import more variables than the API key, including values that redirect API calls.

Mitigation: Only source dotenv files after user authorization, inspect them first, and keep OFOX_API_BASE_URL unset unless testing against a trusted endpoint.

Risk: Endpoint and request overrides can expose the API key or change billable request destinations.

Mitigation: Use the default API endpoint for normal runs and treat OFOX_API_BASE_URL and --extra-json as privileged advanced controls.

Risk: Video generation is billable and failed retries can create duplicate costs.

Mitigation: Use dry-run estimates and an explicit approval gate before billable calls, then resume by polling existing job ids instead of resubmitting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ofox-video-core)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Project homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-video-core)
- [Ofox video API parameter reference](references/api-params.md)
- [Approval gate](references/approval-gate.md)
- [Video pricing](references/pricing.md)
- [Prompt structure for Seedance video jobs](references/prompt-structure.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, API job identifiers, cost summaries, downloaded video files, and JSON sidecars.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create billable Ofox video jobs when a configured API key is present and the user has approved the cost table.]

## Skill Version(s):

1.21.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
