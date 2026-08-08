## Description:

Upscales low-resolution remote sensing imagery with an SRCNN model on CUDA GPUs and produces high-resolution rasters with PSNR/SSIM quality metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to run local 2x, 3x, or 4x super-resolution experiments on single-band remote sensing rasters or synthetic test data, then inspect generated GeoTIFF outputs and restoration quality metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes credential, geocoding, downloader, and cache helper code beyond the stated local super-resolution workflow.

Mitigation: Review the package before installation, install only from a trusted publisher, and prefer a minimized package without those helper modules when they are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-super-resolution-dl)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; runtime outputs include GeoTIFF and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces super_resolved.tif, quality_metrics.json, and output-manifest.json in the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG.md and openai.yaml report 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
