## Description:

Guides Go developers in using the unofficial go-tinker client to access the Thinking Machines Tinker API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add the go-tinker dependency, authenticate with a Tinker API key, and write Go code for model training, sampling, and related API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Tinker API key could be exposed in source code or request logs.

Mitigation: Read the key from TINKER_API_KEY; never hardcode, commit, or log it or request headers.

Risk: A custom endpoint could receive API credentials and requests.

Mitigation: Use the default HTTPS Tinker host unless the user trusts another endpoint.

Risk: Training can consume paid compute, and unloading a model can drop its state.

Mitigation: Run training or model-management calls only when requested and only on models the task created or the user named.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-tinker project linked by the skill](https://github.com/psyb0t/go-tinker)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-tinker)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for an external Go client; no files are produced by the skill itself.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
