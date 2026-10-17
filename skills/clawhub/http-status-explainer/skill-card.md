## Description:

Explain HTTP status codes in plain language and suggest safe next steps for clients and operators debugging APIs, browsers, or reverse proxies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to understand HTTP responses, identify likely causes and responsible teams, and plan safe follow-up checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted HTTP responses may contain credentials or other secrets.

Mitigation: Avoid sharing API keys, cookies, or authorization values; omit any disclosed secrets from replies and advise rotation.

Risk: A status code alone may not reveal the underlying cause.

Mitigation: Treat diagnoses as hypotheses, state assumptions, and confirm against response headers or service logs before acting.

## Reference(s):

- [HTTP Status Explainer on ClawHub](https://clawhub.ai/hmahmadcs/skills/http-status-explainer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with short headings and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Meaning, likely causes, owner, next checks, and a one-line incident update; assumptions identified when details are missing.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
