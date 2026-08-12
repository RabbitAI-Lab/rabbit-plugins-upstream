## Description: <br>
Detects forest loss, gain, and stable areas from multi-temporal NDVI thresholds and change vector magnitude, outputting change rasters and annual area statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and environmental monitoring teams use this skill to classify forest cover loss, gain, and stability from local or synthetic multi-period NDVI rasters and to generate area statistics for forest change ledgers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the main forest-change tool is local, but the package bundles unrelated credential and network helper code, including a hardcoded Earthdata fallback password. <br>
Mitigation: Install only after reviewing the bundled helper code; for normal use, run the documented entrypoint with local files or --synthetic and avoid invoking credential, geocoding, or download helpers unless they have been scoped for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-forest-cover-change) <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and file-output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill's documented agent workflow produces local GeoTIFF change rasters, JSON area statistics, and an output manifest when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
