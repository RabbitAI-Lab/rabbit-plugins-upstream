## Description:

Generates Tongyi Wanxiang 2.7 videos from text prompts, first and last frames, or reference media through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use the skill to request AI video generation from a prompt, frames, or reference images and videos. It returns generated media links and task status through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy, and video generation uses organization credits.

Mitigation: Use --dry-run to preview requests, submit only media approved for cloud processing, monitor credit use, and revoke saved credentials when no longer needed.

## Reference(s):

- [dLazy CLI project page (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video assets with JSON result data, invoked through shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include hosted media URLs; asynchronous requests can return a task identifier and status.]

## Skill Version(s):

1.3.35 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
