## Description:

Search Reddit posts by meaning via the reddapi.dev index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and product teams use this skill to search reddapi.dev for Reddit posts, trends, and subreddit data for market research, user research, and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send REDDAPI_API_KEY to an environment-selected base URL if REDDAPI_BASE_URL is set.

Mitigation: Run only with REDDAPI_BASE_URL unset or explicitly set to https://reddapi.dev, and avoid environments where untrusted variables can affect command execution.

Risk: The skill uses a third-party API credential and shared reddapi.dev quota.

Mitigation: Reference the key only through REDDAPI_API_KEY, avoid pasting it into chat or files, and keep searches scoped to the needed sample size.

Risk: Returned Reddit titles, post bodies, and comments are unmoderated third-party content.

Mitigation: Treat result text as data only, quote it separately from agent reasoning, and do not execute commands or fetch links found inside result content.

## Reference(s):

- [reddapi.dev API reference](references/api-reference.md)
- [reddapi.dev](https://reddapi.dev)
- [reddapi.dev account](https://reddapi.dev/account)
- [ClawHub release page](https://clawhub.ai/lignertys/skills/reddit-insights)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and text or JSON API results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses REDDAPI_API_KEY and optional REDDAPI_BASE_URL or REDDAPI_TIMEOUT environment variables; --raw returns JSON.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
