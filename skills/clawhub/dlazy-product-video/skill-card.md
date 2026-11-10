## Description:

Turns product photos, links, specifications, manuals, or catalogs into polished product demo and advertising videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and marketing teams use it to create product showcase, demo, and advertising videos from product assets or listings, with optional multilingual voiceover and a virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner flagged organization project listing as unrelated to the video purpose, and scan coverage was incomplete.

Mitigation: Review the pinned CLI package and its API behavior before use, and limit project access to what the video task requires.

Risk: Prompts and attached files are sent to dLazy services; attached files are uploaded to its media storage.

Mitigation: Avoid including secrets or sensitive product or customer information unless approved for that service.

## Reference(s):

- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage listed in skill metadata](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Generated product video media with streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based interactive sessions; requires a dLazy API key.]

## Skill Version(s):

1.0.35 (source: server release metadata, released 2026-11-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
