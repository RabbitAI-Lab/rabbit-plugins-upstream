## Description:

ofox-video-core provides a shared Ofox video API execution layer that creates video jobs, polls them to completion, downloads finished MP4 files, and reports actual cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this library skill to call the Ofox video generation API from scenario skills or low-level workflows that need job creation, polling, downloading, cost reporting, and recovery by job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid video generation can incur unexpected cost if a command is run before the user sees the estimate.

Mitigation: Use --dry-run first, show the cost table, and pass --approved only after the user approves the quoted spend.

Risk: OFOX_API_KEY could be exposed or sent to an unintended host if environment files or OFOX_API_BASE_URL are mishandled.

Mitigation: Keep the key out of logs and files, review dotenv contents before sourcing, and treat any non-default API base URL as a host-change warning.

Risk: Real-person reference generation can create rights and consent issues.

Mitigation: Use --real-person true only for references the user is authorized to use, and do not use it for public figures or to bypass moderation.

Risk: Ambiguous create failures can make duplicate submissions possible if retried blindly.

Mitigation: Follow the no-resubmit recovery path: list recent jobs, compare evidence, and poll an existing job when one was likely created.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ofox-video-core)
- [Ofox skill homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-video-core)
- [Ofox app and API key setup](https://app.ofox.ai)
- [API parameter reference](references/api-params.md)
- [Approval gate](references/approval-gate.md)
- [Pricing reference](references/pricing.md)
- [Prompt structure reference](references/prompt-structure.md)
- [Core Ofox video script](references/ofox-video.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated video file paths when commands are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OFOX_API_KEY, curl, and jq; paid generation commands require a cost quote and --approved.]

## Skill Version(s):

2.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
