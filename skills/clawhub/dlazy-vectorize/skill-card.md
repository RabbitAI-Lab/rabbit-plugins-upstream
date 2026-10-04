## Description:

Helps agents convert PNG and JPG images into vectorized assets using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request vectorized versions of logos, icons, and flat illustrations from raster images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images may be uploaded to dLazy's hosted service, and results are hosted there.

Mitigation: Only submit images approved for third-party processing and review service terms before use.

Risk: Authentication saves an API key locally.

Mitigation: Protect local CLI configuration and rotate or revoke the key if exposed.

Risk: The documentation conflicts on required flags and whether output is SVG or PNG.

Mitigation: Check the installed CLI's help and validate the returned file type before relying on the result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a hosted result URL and can optionally save the result locally; the documented SVG claim conflicts with a PNG output example.]

## Skill Version(s):

1.2.24 (source: server release; bundled skill frontmatter says 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
