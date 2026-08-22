## Description:

Plans and runs model, application, media, digital-human, music, Smart Clip, asset, and social-media workflows through a user-configured 算力超市 tenant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[likeadmin-hub](https://clawhub.ai/user/likeadmin-hub)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to plan and execute workflows against a configured 算力超市 tenant while preserving credential, cost, upload, and confirmation boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to a user-configured tenant API using local credentials.

Mitigation: Install only when the tenant and API key scope are trusted, and keep the API key in the configured credential file rather than prompts, URLs, or workflow state.

Risk: Local media uploads can transfer user files to the configured tenant API.

Mitigation: Confirm the tenant destination and the specific file transfer before uploading local media, and use public URLs directly when they are already reachable.

Risk: Social-media and watermark-related operations can affect content rights or platform expectations.

Mitigation: Use these operations only for content the user owns or is authorized to process, and avoid bulk collection workflows.

Risk: Generation and asset operations can spend points or perform destructive changes.

Mitigation: Check tenant availability, validate required fields, compare material price or quality differences, and obtain explicit confirmation before destructive asset deletion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/likeadmin-hub/skills/likeadmin-market-skills)
- [Capability Catalog](references/capability-catalog.json)
- [Contracts Bundle](references/contracts.bundle.json)
- [Intelligent Orchestration](references/orchestration.md)
- [Workflow Inputs](references/workflow-inputs.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON workflow inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tenant discovery guidance, upload confirmations, and non-secret workflow state handling.]

## Skill Version(s):

1.1.0 (source: server release metadata and manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
