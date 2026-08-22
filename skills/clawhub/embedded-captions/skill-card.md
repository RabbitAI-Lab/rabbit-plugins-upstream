## Description:

Adds plain, cinematic, or styled embedded captions to existing single-subject talking-head videos while leaving the source footage otherwise unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media automation agents use this skill to inspect a talking-head clip, choose a caption style identity, generate transcript- and matte-aware caption configuration, run render and QA commands, and deliver captioned MP4 output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can contact GitHub, CDNs, package sources, and model sources, and it can update related installed skills.

Mitigation: Install and run it only in environments where those network contacts and skill updates are acceptable; pre-review or block network paths for offline or sensitive workflows.

Risk: Generated media-processing scripts and newly fetched dependencies may execute during the captioning workflow.

Mitigation: Run the workflow in an isolated project directory or container, and use non-sensitive media unless dependencies and scripts have been reviewed.

Risk: The release security verdict is suspicious despite being mostly purpose-aligned.

Mitigation: Review the skill and security summary before deployment, and require explicit approval before use in production media pipelines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption identity catalog](CATALOG.md)
- [Theme registry](themes/README.md)
- [Rail caption rules](references/rail.md)
- [Composition craft reference](references/composition-craft.md)
- [Failure modes reference](references/failure-modes.md)
- [GSAP CDN dependency](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, media files]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and generated MP4 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project files and either final.mp4 or final_fx.mp4 after local render and composite steps.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
