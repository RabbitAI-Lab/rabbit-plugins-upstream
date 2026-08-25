## Description:

Use FMind as the unified knowledge and external-memory gateway for tenant knowledge-base import and search, L0-L2 memory, context, and published Memory Wiki access through an Agent Binding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[justaboyhai-wq](https://clawhub.ai/user/justaboyhai-wq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill to connect agents to FMind knowledge bases and authorized external memory through environment-based credentials and Agent Binding controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Misconfigured credentials or Agent Binding scopes could expose knowledge or memory outside the intended FMind permissions.

Mitigation: Configure keys through environment variables or a secret manager, use scoped credentials, and review Agent Binding permissions before enabling knowledge or memory access.

Risk: FMind setup keys, runtime keys, user API keys, or signed tokens could be leaked through prompts, logs, URLs, saved files, or shell history.

Mitigation: Do not paste credentials into chat or write them to project files; keep them in secret storage or process environment and avoid printing headers or setup prompts.

Risk: Destructive knowledge-base actions or memory capture could affect unintended resources if an agent acts on ambiguous prompt-supplied identifiers.

Mitigation: Require explicit knowledge-base selection and user confirmation for mutations, respect authorization failures, and do not retry with guessed tenant, team, or resource identifiers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/justaboyhai-wq/skills/fmind)
- [ClawHub publisher profile](https://clawhub.ai/user/justaboyhai-wq)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires FMIND_BASE_URL and FMIND_USER_API_KEY; optional Agent Binding variables enable memory gateway setup and runtime access.]

## Skill Version(s):

2.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
