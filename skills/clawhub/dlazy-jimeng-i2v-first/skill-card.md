## Description:

Generate dynamic Jimeng videos from a single first-frame image and a text prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn a still image and prompt into a Jimeng video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and did not examine the separately installed dLazy CLI; local references were unresolved.

Mitigation: Review the pinned CLI package and confirm you trust dLazy's login flow and hosted service before authenticating.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [JSON result containing generated media URLs or asynchronous task status, with CLI usage in shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 5- or 10-second generation; asynchronous task IDs are available with --no-wait.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
