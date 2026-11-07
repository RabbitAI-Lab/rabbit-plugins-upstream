## Description:

Generates images, videos, and audio by selecting a suitable dLazy CLI model for each request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route image, video, and audio requests to a suitable model and generate or transform media through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy; local media may be uploaded for generation.

Mitigation: Use the skill only for explicit media-generation requests and provide only prompts and media intended for the hosted service.

Risk: Generation can consume account credits.

Mitigation: Check the expected credit use before submitting generation requests.

Risk: The saved dLazy API key grants access to the user's organization.

Mitigation: Protect the saved key and rotate or revoke it when it is no longer needed.

Risk: The external CLI package and hosted service were not fully audited in this review.

Mitigation: Review the CLI package and hosted service against organizational requirements before use.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, JSON]

**Output Format:** [Generated media, typically returned as hosted URLs in a JSON response.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation may consume credits; supplied media can be uploaded to dLazy.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
