## Description:

This skill sends a talking-person video and voice track to Tongyi VideoRetalk to generate a video with lip movements matched to the audio, optionally using a reference face image to select a person.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers can use the dLazy CLI to synchronize a speaker's mouth movements in a video with a replacement voice track, optionally selecting a face when several people appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local video, audio, or reference images are sent to dLazy's hosted service for processing.

Mitigation: Only upload media you are authorized to share and are comfortable sending to the service; review the service terms first.

Risk: Using the CLI requires setting up a dLazy API key.

Mitigation: Keep the key private, use the CLI's supported login flow, and rotate or revoke it if exposed.

Risk: The security scan was partial, could not resolve some local references, and noted a possible mismatch involving the login command it inspected.

Mitigation: Review the skill text and verify the CLI installation and login instructions against the linked source before use.

## Reference(s):

- [CLI source repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files or hosted video URLs, JSON result metadata]

**Output Format:** [Generated media returned through a JSON response, with an optional downloaded file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a talking-person video and voice track; an optional reference face image can select a person.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
