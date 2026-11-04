## Description:

Measures finished AI-made video, image, and audio assets, then ranks takes by measured defects and reference fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative production teams use the skill to review finished AI-generated videos, images, and audio. It produces measured checks with timestamps and evidence, then ranks alternate takes by their detected defects and reference fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional upload_banding.sh helper can execute code embedded in a crafted media filename.

Mitigation: Avoid references/recipes/upload_banding.sh until its filename handling is fixed; use the main judge.py workflow as the security guidance recommends.

Risk: Rerunning into an existing output directory replaces reports and clears evidence JPEGs.

Mitigation: Use a fresh output directory for each run.

Risk: The static assessment did not verify downloaded dependencies, models, or optional external tooling.

Mitigation: Review and pin installation sources before use.

## Reference(s):

- [Project page](https://github.com/vargHQ/skills/tree/main/media-judge)
- [TempGlitch paper](https://arxiv.org/abs/2605.21443)
- [SynFlash paper](https://arxiv.org/abs/2603.17374)
- [Panickssery et al. paper](https://arxiv.org/abs/2404.13076)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown reports, JSON facts, and timestamped evidence images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include measured values and timestamps; outputs vary by video, image, audio, or ranking task. The report also identifies checks that were not run or need visual review.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
