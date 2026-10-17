## Description:

Guides Go developers using the unofficial Black Forest Labs FLUX client to submit image and video tasks, poll results, inspect credits, and manage fine-tunes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go integrations for FLUX image and video generation, poll task results, check credits, and manage fine-tunes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or signed output URLs could be disclosed.

Mitigation: Keep BFL_API_KEY out of logs and source control; validate HTTPS and the provider host before sending credentials or following polling URLs.

Risk: Paid submissions can consume credits, especially when retried after uncertain results.

Mitigation: Confirm paid requests with the user and avoid blindly retrying submissions.

Risk: Deleting a fine-tune changes account state.

Mitigation: Confirm the specific deletion with the user before running it.

## Reference(s):

- [go-bfl on ClawHub](https://clawhub.ai/psyb0t/skills/go-bfl)
- [go-bfl project](https://github.com/psyb0t/go-bfl)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides integration with the API; the skill does not download generated media.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
