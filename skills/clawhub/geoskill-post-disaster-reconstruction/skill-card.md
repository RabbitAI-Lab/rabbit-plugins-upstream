## Description: <br>
Monitors post-disaster reconstruction by classifying building change and recovery progress from multi-temporal high-resolution imagery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and disaster-response teams use this skill to process synthetic scenes or local multi-band GeoTIFF imagery and generate reconstruction progress classifications for affected building areas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helpers can use credentials, read local secret stores, call external geocoding services, cache locations under the home directory, and download arbitrary URLs. <br>
Mitigation: Review the package before sensitive use, remove or isolate helpers that are not needed for the advertised local raster workflow, and run it with least-privilege filesystem and network access. <br>
Risk: The security evidence flags a possibly exposed Earthdata password. <br>
Mitigation: Treat any included Earthdata credential as compromised unless proven otherwise and rotate it before using the package. <br>
Risk: Unpinned dependencies can change behavior across installations. <br>
Mitigation: Pin and review dependencies before deployment in disaster-response or credentialed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-post-disaster-reconstruction) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated local GeoTIFF, JSON, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces progress_class.tif, recovery_progress.tif, reconstruction_params.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
