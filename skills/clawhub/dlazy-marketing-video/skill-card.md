## Description:

Creates marketing, promotional, advertising, and shopping videos from product, brand, brief, or listing inputs for social and campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, ecommerce operators, and agent developers use this skill to start or continue dLazy projects that generate product-focused marketing and shopping videos from briefs, product references, listings, and optional local files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, campaign details, product references, and attached files may be sent to dLazy's hosted service.

Mitigation: Confirm the data-sharing posture is acceptable before installation or invocation, and avoid sending sensitive material unless the user is authorized to share it with dLazy.

Risk: API-key and project-session persistence can retain credentials or prior context between invocations.

Mitigation: Prefer per-invocation authentication where practical, restrict permissions on ~/.dlazy/config.json when saving keys, explicitly select project IDs, and clear sessions when prior context should not be reused.

Risk: The security evidence notes that the local key-permission claim appears under-supported.

Mitigation: Verify local configuration-file permissions before relying on stored-key isolation, and rotate or revoke API keys from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI source link from metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return project-scoped responses and generated media references through the dLazy CLI; local attachments may be uploaded through the service when explicitly passed.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
