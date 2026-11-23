## Description:

Powerful video generation with Kling v3, supporting high-quality text-to-video and image-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to request short videos from Kling v3 with text prompts and optional reference images, then receive the generated media or an asynchronous task result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and reports that the observed action appears limited to `dlazy login`, although the skill describes Kling video generation.

Mitigation: Review the pinned CLI package and service details, and confirm the generation command's behavior before relying on it for video generation.

Risk: Prompts and supplied media are sent to dLazy services, and authentication saves an API key in the local CLI configuration.

Mitigation: Send only prompts and media you are authorized to share, protect the local configuration, and rotate or revoke the API key if needed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [API Calls, Video, Files, JSON]

**Output Format:** [JSON generation results or task status, with generated media available by URL or as a saved file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs and optional saving of generated media to a local path.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
