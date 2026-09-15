## Description:

Ofox Video Core is a library skill that uses the Ofox video API to submit video generation jobs, poll them to completion, download finished MP4 files, and report actual cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill as a shared execution layer for Ofox video generation workflows, especially when a scenario skill has already selected the prompt, model, duration, and resolution. It is also used directly to call low-level Ofox video API parameters or debug and resume existing Ofox video jobs by job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid Ofox API key and can expose it to configurable request destinations.

Mitigation: Keep OFOX_API_BASE_URL unset for real use, do not source untrusted dotenv files, inspect any dotenv file before loading it, and never print or log the raw OFOX_API_KEY value.

Risk: Advanced JSON payload options can bypass normal cost and parameter checks.

Mitigation: Avoid --extra-json unless the final payload is fully understood, run a dry-run cost table first, and require explicit user approval before billable generation.

Risk: Long-running video jobs can be billable even if polling times out or the agent loses track of the job.

Mitigation: Prefer separate create and poll steps when tool timeouts are possible, preserve the returned job id, and check existing Ofox jobs before resubmitting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ofox-video-core)
- [Ofox Video Core homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-video-core)
- [Ofox API key settings](https://app.ofox.ai)
- [Ofox video API parameter reference](references/api-params.md)
- [Approval gate](references/approval-gate.md)
- [Video pricing](references/pricing.md)
- [Prompt structure for Seedance video jobs](references/prompt-structure.md)
- [Creative brief](references/creative-brief.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Files, Guidance, Configuration]

**Output Format:** [Markdown guidance with bash commands, status text, JSON payload details, downloaded MP4 files, and cost reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, and jq; billable generation should be preceded by dry-run cost review and explicit approval.]

## Skill Version(s):

1.24.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
