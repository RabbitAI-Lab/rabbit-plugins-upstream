## Description:

ofox-video-core is a library skill that helps agents submit Ofox video generation jobs, poll for completion, download MP4 results, and report costs for low-level API calls or dependent scenario skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this library skill when they need low-level access to the Ofox video API, including creating, resuming, pricing, batching, chaining, and downloading video jobs. Scenario skills can depend on it to avoid duplicating API and cost-control behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential handling or environment redirection could expose the API key or send requests to an unintended API base.

Mitigation: Keep OFOX_API_BASE_URL unset for real use, never source an untrusted .env file, never print OFOX_API_KEY, and review the shell script and command environment before execution.

Risk: The skill can submit paid video generation jobs.

Mitigation: Require the dry-run cost table and explicit approval before any billable request, and avoid resubmitting after ambiguous create failures.

Risk: Advanced extra JSON fields can alter API request behavior beyond the normal flags.

Mitigation: Use --extra-json only for clearly understood fields and review the generated request before paid execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ofoxai/skills/ofox-video-core)
- [Ofox Publisher Profile](https://clawhub.ai/user/ofoxai)
- [Skill Homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-video-core)
- [Ofox App and API Keys](https://app.ofox.ai)
- [Ofox Video API Parameter Reference](references/api-params.md)
- [Approval Gate](references/approval-gate.md)
- [Pricing Reference](references/pricing.md)
- [Prompt Structure](references/prompt-structure.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands; API executions can produce MP4 files and JSON sidecars.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY for paid API execution and uses curl and jq; dry-run cost review and explicit approval are expected before billable jobs.]

## Skill Version(s):

1.27.1 (source: frontmatter, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
