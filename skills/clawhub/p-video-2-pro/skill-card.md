## Description:

Use when someone wants a cinematic clip from text or start/end frames - product ads, documentary shots, or dialogue with generated audio; not for 1080p, imported audio tracks, or talking-head-only hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to guide an agent through one Pruna p-video-2-pro video-generation request from text, a first frame, or first and last frames. It helps prepare prompts, required parameters, API calls, and routing decisions for cinematic clips with generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected frame images are sent to Pruna's paid API.

Mitigation: Confirm the user approves the prompt, input frames, cost-bearing settings, and Pruna data sharing before making an API request.

Risk: The skill suggests unpinned npx installs for related skills.

Mitigation: Pin or review related skill sources before installation in environments with supply-chain controls.

Risk: Requests outside the documented model boundary can produce the wrong workflow or failed API calls.

Mitigation: Route 1080p, imported audio, draft previews, talking-head-only, existing-footage edits, and multi-scene requests to the alternate skills named in the artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-2-pro)
- [Pruna file upload endpoint](https://api.pruna.ai/v1/files)
- [Pruna prediction endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one p-video-2-pro prediction workflow; generated media is returned by Pruna API, not by the skill itself.]

## Skill Version(s):

1.0.13 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
