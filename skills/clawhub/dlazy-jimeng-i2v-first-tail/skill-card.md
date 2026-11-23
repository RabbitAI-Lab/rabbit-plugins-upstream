## Description:

Generate coherent transition videos using Jimeng's first and tail frame models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators can provide a prompt and first and last frame images to generate a coherent transition video with Jimeng.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted that the documented login command was not clearly connected to the stated video-generation purpose.

Mitigation: Confirm the CLI's authentication flow in publisher documentation before logging in.

Risk: The security review reported that some installation and endpoint references were not resolved.

Mitigation: Verify the package and API destinations against current publisher documentation before installing or sending content.

Risk: Prompts and local media supplied for generation are sent to the hosted service, and generated media is returned through hosted URLs.

Mitigation: Send only prompts and media that are appropriate for processing by the service, and review the service terms before use.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video, JSON metadata]

**Output Format:** [Hosted media asset URL with JSON result and task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a task identifier for asynchronous generation; results may be saved to a local path.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
