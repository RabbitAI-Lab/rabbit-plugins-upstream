## Description:

Search X/Twitter through OpenClaw's native OAuth-backed xAI x_search tool, with an optional JavaScript CLI wrapper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search X/Twitter through OpenClaw's OAuth-backed xAI integration, inspect posts or trends, and produce cited summaries or CLI search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI executable override can run an unexpected OpenClaw binary if a user supplies an untrusted --openclaw-bin path or X_SEARCH_OAUTH_OPENCLAW_BIN value.

Mitigation: Use the default OpenClaw executable or only set the override to a trusted, exact executable path.

Risk: Returned X/Twitter posts are untrusted external content and may contain misleading claims or prompt-like instructions.

Mitigation: Treat post content as evidence only, cite original returned X URLs, separate observations from inference, and confirm important claims with first-party sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leostehlik/skills/x-search-oauth)
- [OpenClaw xAI provider documentation](https://docs.openclaw.ai/providers/xai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance and CLI text or JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search reports should cite original X URLs when returned by x_search; CLI output can be normalized JSON with --json.]

## Skill Version(s):

0.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
