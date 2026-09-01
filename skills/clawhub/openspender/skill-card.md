## Description:

OpenSpender lets agents spend from a user-funded allowance to call paid web services such as search, model, media generation, and x402/MPP catalog routes, with pricing and budget caps surfaced before paid calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openspender](https://clawhub.ai/user/openspender)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to give an agent a capped paid-access route for web search, model calls, media generation, public file pinning, and other cataloged APIs when the user's own free tools or API keys do not cover the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can spend from a user-funded allowance, and normal paid calls may proceed without per-call confirmation inside configured caps.

Mitigation: Use small per-request, daily, total, and host caps; surface prices and denials to the user; require explicit approval for unusual or higher-cost tasks.

Risk: Public file-upload and media routes can send files, URLs, prompts, or generated assets to third-party services.

Mitigation: Avoid private or sensitive inputs unless the user accepts third-party processing, and require explicit confirmation before uploads.

Risk: Duplicate media submissions or blind retries after a settled failure can create duplicate paid jobs.

Mitigation: Inspect routes before paid calls, poll pending jobs instead of resubmitting them, and do not retry settled failures without showing the transaction context to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/openspender/skills/openspender)
- [OpenSpender homepage](https://openspender.com)
- [OpenSpender protocol reference](https://openspender.com/llms.txt)
- [Canonical OpenSpender skill](https://openspender.com/SKILL.md)
- [OpenSpender remote MCP connector](https://openspender.com/api/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands, API request examples, and cost-reporting text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paid request receipts, denial details, polling instructions, and task-level spend summaries.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
