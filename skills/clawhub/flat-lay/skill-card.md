## Description:

Transforms clothing flat-lay and pose/reference images into on-model e-commerce product photos while preserving garment style, color, texture, and fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, creative teams, and agents use this skill to prepare try-on and catalog imagery from garment photos, pose references, and optional model references. Outputs should be reviewed for garment fidelity, model likeness rights, and product accuracy before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, reference, and model images are uploaded to the selected cloud image provider for generation.

Mitigation: Use only images that the user is allowed to upload, avoid sensitive personal imagery, and confirm provider data-handling requirements before use.

Risk: The optional ARK_BASE_URL setting can redirect image data and an API key to a nonstandard endpoint.

Mitigation: Leave ARK_BASE_URL unset unless the endpoint is fully trusted, and prefer official HTTPS provider endpoints with narrowly scoped, revocable API keys.

Risk: Documented npx and GitHub install flows execute remote code.

Mitigation: Verify the publisher and pin reviewed versions before installing or running the skill in sensitive environments.

Risk: Generated try-on imagery can alter or reuse a person's likeness in a way that implies endorsement.

Mitigation: Use only model/reference images with appropriate rights and consent, and review outputs to avoid misleading commercial endorsement or impersonation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy product site](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash commands and optional JSON output from generation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or saves JPEG image files through cloud image providers; the default flat-lay task uses 1024x1536, high quality output.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
