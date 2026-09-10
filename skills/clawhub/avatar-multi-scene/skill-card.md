## Description:

Use when someone wants the same person hosting several clips \u2014 multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to plan and produce multi-scene avatar or mixed avatar-and-animation reels with a continuous host, staged approvals, Pruna generation calls, and ffmpeg assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses external Pruna services and may upload selected media references.

Mitigation: Use the skill only when Pruna service use is intended, confirm PRUNA_API_KEY handling, and verify that all uploaded references are owned or licensed.

Risk: Generation calls can spend API credits or create user-visible media before the user has approved the plan, stills, and clips.

Mitigation: Preserve the documented phase gates and do not call prediction endpoints until the corresponding approval is explicit.

Risk: ffmpeg examples can overwrite local render files.

Mitigation: Review output paths before running shell commands and write renders into a deliberate project output directory.

Risk: Package-install commands add related skills and dependencies to the local agent environment.

Mitigation: Install only the Pruna skills needed for the requested workflow and review install commands before execution.

Risk: Motion-transfer rows can produce poor or misleading results when the source video and reference image are badly aligned.

Mitigation: Check pose, shot size, facing direction, limb visibility, and media rights before running p-video-animate; repose or choose a closer template when alignment is weak.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/avatar-multi-scene)
- [prompt-templates.md](artifact/prompt-templates.md)
- [animate-beats.md](artifact/animate-beats.md)
- [examples.md](artifact/examples.md)
- [batch.template.json](artifact/templates/batch.template.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON snippets, API-call structure, and inline bash or ffmpeg commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local manifest paths and MP4 render paths after user approval gates and Pruna generation steps.]

## Skill Version(s):

1.0.11 (source: evidence release and artifact frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
