## Description:

Text-to-vector model that outputs SVG results. Suitable for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can request scalable vector artwork such as logos and icons using a text prompt, then save or use the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial and could not resolve some referenced paths or install details.

Mitigation: Review the complete skill instructions and package details before installing.

Risk: Prompts and any local files supplied to the generation workflow are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive prompts or files unless the service's data handling terms are acceptable for your use.

Risk: The CLI requires an API key, which is stored in its local configuration when using the documented login flow.

Mitigation: Use an appropriately scoped key and rotate or revoke it if it may have been exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy service website](https://dlazy.com)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Vector artwork, Images, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated image or vector asset with a JSON result envelope containing its URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can run asynchronously; the CLI can save the returned asset to a local path.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
