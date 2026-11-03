## Description:

script to video, screenplay to video, shot list to video — turn a script into a storyboarded, shot-by-shot video: break down scenes, generate shots, assemble, validate. Use when the user gives a script or scene breakdown and wants a video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn a script or shot list into a multi-shot video, including a storyboard, generated shots, and an assembled render. It can start a new video project or continue an existing one.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scripts and selected attachments are sent to dLazy, and using the service may spend account credits.

Mitigation: Share only content approved for the service, review attachments before sending, and check available credits before starting generation.

Risk: Login stores an organization API key in the local CLI configuration, and the external CLI package and hosted backend were not independently audited.

Mitigation: Use an organization key you are authorized to manage, protect the local configuration, and revoke or rotate the key from the dashboard if needed.

## Reference(s):

- [CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance]

**Output Format:** [Rendered video files with accompanying storyboard, shot details, and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation and rendering depend on the user's prompts, selected attachments, and available service credits.]

## Skill Version(s):

1.0.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
