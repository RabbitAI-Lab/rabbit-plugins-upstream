## Description:

WRouter Provider helps agents configure and use WRouter as an OpenAI-compatible LLM gateway for model discovery, chat/completions, embeddings, image calls, and common client integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrouter](https://clawhub.ai/user/wrouter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to route OpenAI-compatible clients through WRouter, configure credentials, discover enabled models, and troubleshoot gateway authentication or model availability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reads a WRouter API token from local configuration.

Mitigation: Use a dedicated API token, keep the credentials file private, and restrict permissions such as with chmod 600.

Risk: Prompts and request data are sent to the third-party WRouter gateway when the helper is explicitly used.

Mitigation: Confirm WRouter is trusted for the data being sent and review the configured base URL before use.

## Reference(s):

- [WRouter API base URL](https://wrouter.ai/v1)
- [WRouter service](https://wrouter.ai)
- [ClawHub skill page](https://clawhub.ai/wrouter/skills/wrouter-provider)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell, Python, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for the bundled helper script and can use ~/.config/wrouter/credentials for local WRouter settings.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
