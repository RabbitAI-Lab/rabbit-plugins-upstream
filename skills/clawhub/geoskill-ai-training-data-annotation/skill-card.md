## Description: <br>
Small U-Net binary semantic segmentation for remote-sensing pre-labeling with active-learning uncertainty sampling, producing COCO and GeoJSON annotations plus an uncertainty raster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial annotation teams use this skill to pre-label local or synthetic remote-sensing imagery, identify uncertain regions for manual review, and export annotation artifacts for training-data workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential, geocoding, downloader, and hardcoded-password code may add risk outside the local annotation workflow. <br>
Mitigation: Review or remove those helpers before installation when only local annotation is needed. <br>
Risk: The security evidence reports an exposed Earthdata credential. <br>
Mitigation: Rotate the exposed credential before use and avoid running with unnecessary credential access. <br>
Risk: Unpinned dependencies can change runtime behavior over time. <br>
Mitigation: Pin and review dependencies before production deployment. <br>
Risk: The skill can include network-capable helpers even though the main synthetic workflow runs locally. <br>
Mitigation: Run it in a restricted environment for offline annotation workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-ai-training-data-annotation) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [PyTorch CUDA wheel index](https://download.pytorch.org/whl/cu121) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples and generated JSON, GeoJSON, GeoTIFF, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces COCO annotations, GeoJSON pre-labels, an uncertainty GeoTIFF, and an output manifest in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: target metadata and server release; artifact changelog reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
