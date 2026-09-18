## Description:

Helps an agent brief, price, and generate deliberately unpolished, phone-shot UGC-style product videos for unboxings, first impressions, and customer-style reviews through Ofox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to create short synthetic UGC-style product clips when a real-looking unboxing, first-impression, or review-style ad is needed. It is intended for disclosed synthetic advertising rather than fabricated customer testimony or undisclosed endorsements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Synthetic UGC-style ads may be mistaken for real customer footage or endorsements.

Mitigation: Use the skill only for clearly disclosed synthetic advertising, and avoid fabricated customer reviews or undisclosed endorsements.

Risk: The skill depends on OFOX_API_KEY for paid Ofox video generation.

Mitigation: Keep OFOX_API_KEY only in the execution environment, do not paste it into prompts or logs, and review costs before approving paid runs.

Risk: The security summary identifies overbroad, unpinned recovery install commands.

Mitigation: Avoid wildcard global npx install paths unless the source, scope, and version have been separately verified and accepted.

Risk: Quality evidence is thin: the scenario documents one paid run, and some routes remain outside that measured setup.

Mitigation: Start with a small draft, review delivered frames before shipping, and treat attached-photo, person-on-camera, speech, longer-duration, or higher-tier runs as experiments.

Risk: Prompts can unintentionally produce polished ad footage, visible filming devices, anatomy issues, or music-related moderation failures.

Mitigation: Review the prompt for polish words, describe the capture as a viewpoint rather than a device location, prefer simple hands-only action chains, and request ambient/action sounds instead of music.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ugc-ads)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [ugc-ads homepage](https://github.com/ofoxai/skills/tree/main/skills/ugc-ads)
- [Ofox API keys](https://app.ofox.ai)
- [ofox-video-core prompt structure](../ofox-video-core/references/prompt-structure.md)
- [ofox-video-core creative brief](../ofox-video-core/references/creative-brief.md)
- [ofox-video-core approval gate](../ofox-video-core/references/approval-gate.md)
- [ofox-video-core API parameters](../ofox-video-core/references/api-params.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise brief recaps, cost tables, prompt text, and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report Ofox job status, real cost, and an absolute VIDEO_PATH after generation.]

## Skill Version(s):

1.0.2 (source: frontmatter, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
