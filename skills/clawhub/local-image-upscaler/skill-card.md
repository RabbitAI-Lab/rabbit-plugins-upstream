## Description: <br>
Upscale, inspect, or compress JPG, PNG, or WebP images locally on macOS or Windows with selectable profiles, resolution presets, batch folders, offline cache reuse, and verified download fallbacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[harven-droid](https://clawhub.ai/user/harven-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and image-processing users use this skill to inspect, upscale, batch-process, and compress local JPG, PNG, and WebP images while keeping image files on device. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads and runs a pinned third-party Upscayl runtime and model files. <br>
Mitigation: Use trusted mirrors or prefilled offline caches, and keep the documented SHA-256 verification enabled before setup and every upscale. <br>
Risk: Batch processing or overwrite options can write many output files or replace existing outputs. <br>
Mitigation: Review output paths before batch jobs, use dry-run for compression batches, and use --overwrite only when replacement is intentional. <br>
Risk: AI upscaling reconstructs texture and may create apparent detail that was not present in the source image. <br>
Mitigation: Describe enhanced output as reconstruction, not factual recovery, and avoid using it as forensic proof of source details. <br>
Risk: Redistributing downloaded runtime or model files may trigger separate upstream license and notice obligations. <br>
Mitigation: Review the upstream Upscayl runtime and model terms before redistribution and keep applicable notices with redistributed artifacts. <br>


## Reference(s): <br>
- [Algorithm Profiles](references/algorithms.md) <br>
- [Platform and Storage Reference](references/platforms.md) <br>
- [Upstream Licenses and Attribution](references/licenses.md) <br>
- [Upscayl NCNN runtime](https://github.com/upscayl/upscayl-ncnn) <br>
- [Upscayl model files](https://github.com/upscayl/upscayl/tree/main/resources/models) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands, local image output files, and optional JSON inspection reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local image files and inspection/compression reports; does not upload user images.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
