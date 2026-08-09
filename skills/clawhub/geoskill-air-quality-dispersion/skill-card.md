## Description: <br>
Simulates point-source pollutant concentration fields with a Gaussian plume model, Pasquill-Gifford/Briggs stability parameters, and optional DEM terrain correction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, environmental analysts, and GIS practitioners use this skill to estimate ground-level pollutant dispersion for industrial-park impact assessment, stack siting, and rapid exposure analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence reports under-disclosed network, geocoding, caching, and credential-handling helper code outside the advertised offline simulator path. <br>
Mitigation: Review before installing on machines with sensitive project directories, ~/.netrc, or ~/.geoskill/secrets.json; run only the intended offline simulator path unless the helper behavior is explicitly needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-air-quality-dispersion) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Release changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Configuration, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF, JSON, Markdown guidance, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces concentration.tif, dispersion_params.json, and output-manifest.json for simulator runs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
