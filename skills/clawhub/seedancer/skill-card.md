## Description:

Seedancer is an AI film-director workflow that turns scripts into production-ready image and video prompts, story analysis, creative baselines, asset plans, shot sequences, bilingual JSON prompts, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, filmmakers, and developers use Seedancer to analyze scripts, plan characters and props, design shot groups, and produce model-specific prompts for image and video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real-person photos, videos, voice, client material, or confidential scripts may be uploaded to external services during production workflows.

Mitigation: Require the agent to show which files will be uploaded, the provider or domain, the purpose, expected cost, and whether user consent or redaction is needed before proceeding.

Risk: Project assets and .seedancer state may persist after use without enough privacy detail.

Mitigation: Before using sensitive material, require a deletion plan for stored assets and state files and confirm that unnecessary retained files are removed.

Risk: The workflow can drive costly image, video, audio, and analysis generation steps.

Mitigation: Use the documented cost-gate flow to estimate cost, request explicit confirmation, and record actual usage before running generation batches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/seedancer)
- [README](README.md)
- [Release notes](release-notes.md)
- [Changelog](CHANGELOG.md)
- [Scene prototype router](references/scene-prototypes.md)
- [Camera-emotion sync](references/camera-emotion-sync.md)
- [Performance micro-beats](references/performance-micro-beats.md)
- [JSON API output mode](references/json-api-mode.md)
- [Lighting rules](references/lighting-rules.md)
- [Asset whitelist](references/asset-whitelist.md)
- [Cost gates](references/cost-gates.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, configuration]

**Output Format:** [Markdown guidance, bilingual prompt text, optional JSON arrays, and structured production checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model-specific constraints, asset references, cost gates, QA checks, and project state guidance.]

## Skill Version(s):

7.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
