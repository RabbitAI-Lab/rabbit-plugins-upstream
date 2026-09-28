## Description:

Generates a lip-synced video from supplied video and audio for dubbing, localization, and virtual presenters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to synchronize a speaker's lip movements in a video with supplied audio for dubbing, localization, or virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied video and audio are uploaded to the dLazy service for processing.

Mitigation: Submit only media you are authorized to share with the service.

Risk: Installing the pinned third-party CLI and saving an API key locally require trust in the package and service.

Mitigation: Review @dlazy/cli@1.2.3 before use; prefer npx for an on-demand install and DLAZY_API_KEY if you do not want to save the key.

Risk: Some command and output examples appear to be copied from another workflow and may be inaccurate.

Mitigation: Confirm arguments and result shape with dlazy sync-lipsync-3 -h and the actual CLI response.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy service returns a generated media URL; the CLI can save the resulting video locally.]

## Skill Version(s):

1.3.22 (source: server-resolved ClawHub release; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
