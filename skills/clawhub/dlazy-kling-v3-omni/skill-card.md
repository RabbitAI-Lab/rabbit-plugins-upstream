## Description:

Provides CLI guidance for requesting Kling v3 Omni video generation through dLazy using prompts and supported media references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use it to request Kling v3 Omni video generation from prompts and image or video references through dLazy's CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment did not demonstrate the advertised video-generation flow and reported that the supplied skill mainly runs a dLazy login flow.

Mitigation: Verify the CLI's actual operation and review the account access and API-key scope before authenticating.

Risk: The assessment is incomplete because some referenced installation and configuration details were unresolved.

Mitigation: Check the pinned CLI package and its local credential handling before installation, and keep API keys private.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)

## Skill Output:

**Output Type(s):** [Video assets, JSON result metadata]

**Output Format:** [Hosted media URLs and JSON result or asynchronous task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a task identifier for later status checks; results can be saved to a local path.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
