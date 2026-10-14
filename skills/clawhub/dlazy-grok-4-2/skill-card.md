## Description:

Helps agents generate text, answer questions, and reason through prompts using the dLazy-hosted Grok 4.2 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to request text generation, conversational answers, and reasoning through the dLazy Grok 4.2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms such as chat or QA may invoke the hosted service unexpectedly.

Mitigation: Invoke explicitly for Grok or dLazy tasks and confirm before sending user content.

Risk: Prompts, parameters, and explicitly supplied media files are sent to dLazy's hosted service.

Mitigation: Avoid sharing sensitive content or files unless the user approves the transfer.

Risk: The CLI can store an API key locally and requires installing a third-party package.

Mitigation: Review the package before installation; use DLAZY_API_KEY per run if local key storage is unwanted.

Risk: The documented image/file example conflicts with the text-generation use case.

Mitigation: Check actual response types and file-handling behavior before relying on results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may include asynchronous task IDs or hosted output URLs; the documented example shows an image despite the text-focused description.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; bundled frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
