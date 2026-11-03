## Description:

Generates videos with Kling v3 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate videos from text prompts or reference images, then retrieve the hosted result or save it locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy, and generation may incur charges.

Mitigation: Use only media you are comfortable sending and review the generation cost before proceeding.

Risk: The CLI stores an API credential locally; the external CLI and hosted service were not fully audited.

Mitigation: Prefer device login, protect the saved credential, and revoke it when no longer needed. Review vendor terms before sharing sensitive content.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy website](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video, URLs, Files]

**Output Format:** [Hosted video URL in a JSON response; optionally a saved local video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before the video is ready.]

## Skill Version(s):

1.3.37 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
