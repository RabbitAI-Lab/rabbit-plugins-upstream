## Description:

Wraps the a7w flashvsr video super-resolution APIs so an agent can submit video upscaling jobs and query task results using the user's api.a7w.cn API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to configure an a7w API key, submit hosted video super-resolution jobs, and poll task status or results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can save and use an a7w API key for broader marketplace calls, which may expose account balance if the key is leaked or overused.

Mitigation: Use a limited or disposable API key where possible, avoid committing keys, store local credentials with restricted permissions, and revoke or rotate keys after suspected exposure.

Risk: The client supports alternate hosts through --host or A7W_HOST, so credentials could be sent away from the intended a7w service if misconfigured.

Mitigation: Use the default https://api.a7w.cn endpoint unless you control the alternate endpoint, and review command lines and environment variables before execution.

Risk: Submitting and polling video upscaling tasks can spend account balance, and duplicate submissions may incur duplicate charges.

Mitigation: Review the documented pricing, check parameters with the schema command, use --no-wait when appropriate, and avoid resubmitting the same input unless a new paid run is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-flashvsr)
- [Getting started](references/getting-started.md)
- [Submit API reference](references/api-submit.md)
- [Query API reference](references/api-query.md)
- [General a7w plugin notes](references/通用说明.md)
- [a7w API service](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown documentation with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided A7W_API_KEY or local ~/.a7w/config.json; API calls can consume account balance.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
