## Description:

Routes broad research, search, scraping, monitoring, marketplace, social, travel, jobs, maps, and competitive-intelligence requests to the smallest suitable Dataify skill set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to turn outcome-oriented requests into a minimal Dataify capability plan and execution path for discovery, scraping, monitoring, or structured data collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad research, scraping, monitoring, multi-page, media-heavy, or competitive-intelligence requests can consume Dataify API credits.

Mitigation: Review task scope and require confirmation for higher-volume, multi-page, media-download, or materially credit-sensitive work.

Risk: API tokens can be exposed if placed in chat, commands, or project files.

Mitigation: Keep DATAIFY_API_TOKEN in the environment and never print or embed token values in generated commands or output.

Risk: Asynchronous Builder jobs may leave work incomplete if only the task is submitted.

Mitigation: Use task lifecycle handling to wait for and return collected results unless the user explicitly requests submission-only behavior.

## Reference(s):

- [Dataify capability map](references/capability-map.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-router)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or concise text with optional shell commands and source coverage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source coverage, limitations, asynchronous task state, and relevant refinements.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
