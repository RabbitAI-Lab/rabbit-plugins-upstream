## Description:

Separates image foregrounds from backgrounds and returns a transparent-background image URL for product images, portraits, and compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams can remove image backgrounds for product imagery, portrait cutouts, and compositing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to dLazy for cloud processing and may contain sensitive content.

Mitigation: Only submit images approved for cloud processing; avoid sending sensitive images when their handling is uncertain.

Risk: Authentication stores an API key in the local CLI configuration, and requests can consume service credits.

Mitigation: Protect the local configuration and keep credentials out of shared logs; monitor credit use and revoke or rotate a key if exposed.

## Reference(s):

- [CLI project listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response containing a transparent-background image URL and image metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The resulting image is hosted by dLazy and can optionally be saved to a local path.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
