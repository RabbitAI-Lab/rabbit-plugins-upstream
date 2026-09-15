## Description:

Requires OFOX_API_KEY; helps an agent turn a script beat or scene description into a realistic, dialogue-driven short-drama video prompt, cost estimate, and Ofox generation workflow using Seedance 2.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to turn dialogue-heavy short-drama beats into structured prompts, approval-ready cost estimates, and Ofox video-generation commands. It is intended for realistic human scenes with spoken dialogue, not silent product footage, anime-style scenes, or multi-job editing/stitching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance can install unpinned external skills globally across agents.

Mitigation: Install only the required ofox-video-core dependency from a trusted, pinned source and avoid wildcard global installer commands.

Risk: The skill sends scripts, dialogue, and referenced assets to Ofox for paid generation.

Mitigation: Avoid confidential material and use real-person likenesses only with approval and rights before submitting a generation job.

Risk: Generated jobs can incur cost and may fail moderation or model constraints.

Mitigation: Use the documented approval gate and cost estimate before paid submission, then rely on the core skill's polling and error-handling flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-short-drama)
- [Skill homepage from release metadata](https://github.com/ofoxai/skills/tree/main/skills/seedance-short-drama)
- [Ofox app and API key management](https://app.ofox.ai)
- [Ofox models catalog API](https://api.ofox.ai/v1/models/catalog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured prompt text, approval tables, and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY plus curl and jq; may submit paid Ofox video-generation jobs after user approval and report job status, download path, and actual cost.]

## Skill Version(s):

1.13.1 (source: server release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
