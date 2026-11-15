## Description:

script to video, screenplay to video, shot list to video — turn a script into a storyboarded, shot-by-shot video: break down scenes, generate shots, assemble, validate. Use when the user gives a script or scene breakdown and wants a video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators can submit a screenplay or scene breakdown to create a multi-shot storyboarded video, including generated shots and assembled output. They can continue work in a project across multiple turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with the CLI are sent to dLazy's hosted API and media storage.

Mitigation: Only submit scripts and files that are appropriate to share with the service, and confirm the intended organization and project before sending them.

Risk: The security guidance notes that CLI login and project-listing actions are reported, while their connection to script-to-video generation is not demonstrated.

Mitigation: Review the CLI project and installation details before granting credentials, and use an organization-scoped key that can be rotated or revoked.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands, Configuration instructions]

**Output Format:** [Generated video assets and text responses, with command examples in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn workflow; requires a dLazy API key.]

## Skill Version(s):

1.0.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
