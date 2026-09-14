## Description:

Requires OFOX_API_KEY; turns novel or script excerpts into anime-style storyboard video clips by generating character opening frames with Ofox image APIs and using those frames to start Ofox video shots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn story, novel, or script excerpts into anime-style video shots or short storyboard sequences with image-based character consistency. It is intended for anime-styled character scenes, not realistic-human dialogue, product footage, or multi-character image-lock workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags overbroad global install guidance.

Mitigation: Install only the required Ofox core skills from the same trusted publisher or another trusted, pinned source, rather than following a wildcard global install command.

Risk: The security review flags moderation-bypass-style model guidance.

Mitigation: Treat model-selection notes as compatibility and cost guidance only; do not use them to bypass copyright or safety refusals.

Risk: Prompts and media are sent to Ofox and upstream generation providers.

Mitigation: Review inputs for sensitive, confidential, or restricted content before use, and proceed only when provider processing is acceptable.

Risk: The workflow can submit paid image and video generation jobs.

Mitigation: Use the documented dry-run estimates and require explicit user approval before each paid image or video phase.

Risk: Generated anime prompts or attached frames may trigger copyright or safety moderation failures.

Mitigation: Revise prompts toward permitted original content, avoid asking the model to generate music or copyrighted-style material, and follow the documented no-resubmit guidance for ambiguous failures.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ofoxai/skills/seedance-anime-drama)
- [Publisher Profile](https://clawhub.ai/user/ofoxai)
- [Skill Homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-anime-drama)
- [Ofox API Key Portal](https://app.ofox.ai)
- [Ofox Models Catalog](https://api.ofox.ai/v1/models/catalog)
- [ofox-video-core creative brief reference](../ofox-video-core/references/creative-brief.md)
- [ofox-video-core prompt structure reference](../ofox-video-core/references/prompt-structure.md)
- [ofox-video-core approval gate reference](../ofox-video-core/references/approval-gate.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, approval tables, prompt text, and generated asset paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dry-run cost estimates, explicit approval gates, OFOX_API_KEY, curl, jq, and delegated Ofox image/video core skills.]

## Skill Version(s):

1.12.1 (source: server release metadata, artifact frontmatter, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
