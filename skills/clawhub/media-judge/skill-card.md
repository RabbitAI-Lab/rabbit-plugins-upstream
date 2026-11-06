## Description:

Judge finished AI-made video, image, or audio by measuring defects and ranking takes from the findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to review finished videos, images, and audio, produce timed measurements with evidence, and rank alternate takes by detected defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional upload-banding recipe can execute code embedded in a crafted media filename.

Mitigation: Avoid references/recipes/upload_banding.sh until filenames are passed as data rather than inserted into Python code.

Risk: Rerunning into an existing output directory replaces reports and removes existing evidence JPEGs.

Mitigation: Use a fresh output directory for each run.

Risk: Dependency packages and downloaded models were not executed or audited in the static review.

Mitigation: Install only media-judge unless the broader bundle is needed, and review dependency downloads.

## Reference(s):

- [Media Judge project](https://github.com/vargHQ/skills/tree/main/media-judge)
- [TempGlitch](https://arxiv.org/abs/2605.21443)
- [SynFlash](https://arxiv.org/abs/2603.17374)
- [Panickssery et al. on self-preference in model evaluations](https://arxiv.org/abs/2404.13076)
- [WCAG 2.2: Three Flashes or Below Threshold](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Images]

**Output Format:** [Markdown reports, JSON measurements, and image evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timed findings with measured values and evidence; take rankings are based on defect counts, not a single quality score.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
