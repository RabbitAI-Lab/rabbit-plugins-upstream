## Description: <br>
Calculate spectral indices from GeoTIFF imagery using pure Python. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to calculate vegetation, water, urban, burn, bare-soil, and custom spectral indices from local GeoTIFF imagery through command-line workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Undisclosed helper modules can make third-party network geocoding calls and cache place-query data under the user's home directory. <br>
Mitigation: Use only the documented local GeoTIFF calculation workflow unless network geocoding and local caching are acceptable; review any use of _place.py or _geoskill_core.aoi before deployment. <br>
Risk: The package includes generic download helpers that can fetch arbitrary URLs. <br>
Mitigation: Do not invoke _geoskill_core.safe_download unless the URL source, destination path, expected size, and checksum policy are reviewed. <br>
Risk: CLI output paths can replace existing files. <br>
Mitigation: Run with explicit output paths in a controlled working directory and treat pre-existing output files as replaceable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/rs-index-calc) <br>
- [Skill instructions](SKILL.md) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and code references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The underlying tool writes single-band GeoTIFF outputs and may print index statistics or JSON QA summaries when invoked.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
