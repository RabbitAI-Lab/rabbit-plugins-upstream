## Description:

Shared execution layer for the Ofox video generation API that creates video jobs, polls them to completion, downloads finished MP4 outputs, and reports actual cost for scenario skills or low-level Ofox API use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this library skill to run paid Ofox video generation jobs from higher-level scenario skills, including job creation, polling, result download, cost reporting, batching, chaining, and troubleshooting by job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Ofox billing credential and request data can be sent to a non-Ofox endpoint if OFOX_API_BASE_URL is set to an untrusted target.

Mitigation: Before running paid generation, verify OFOX_API_BASE_URL is unset or intentionally points to a trusted endpoint.

Risk: Sourcing a dotenv file as shell code can import more variables than just OFOX_API_KEY.

Mitigation: Avoid repository-provided dotenv files; when the user authorizes a dotenv, inspect it first and never echo secret values.

Risk: Paid video generation can spend credits once a job is submitted.

Mitigation: Use the documented dry-run cost table and require explicit user approval before any billable request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ofox-video-core)
- [Ofox Video Core source homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-video-core)
- [Ofox API key portal](https://app.ofox.ai)
- [Ofox video API endpoint](https://api.ofox.ai/v1/videos)
- [Ofox video API parameter reference](references/api-params.md)
- [Approval gate](references/approval-gate.md)
- [Video pricing](references/pricing.md)
- [Prompt structure for Seedance video jobs](references/prompt-structure.md)
- [Creative brief](references/creative-brief.md)
- [Ofox video shell client](references/ofox-video.sh)
- [Model snapshot fallback](references/models-snapshot.json)
- [Pricing snapshot fallback](references/pricing-snapshot.json)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash commands, CLI status lines, MP4 video files, and JSON metadata sidecars]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY for paid generation; model and pricing discovery plus dry-run estimates can run without the key.]

## Skill Version(s):

1.21.3 (source: frontmatter, changelog, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
