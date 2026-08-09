## Description: <br>
Multi-hazard probability times asset value times vulnerability curves to compute expected loss for insurance risk mapping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and insurance risk teams use this skill to compute multi-hazard expected annual loss from asset, hazard, and vulnerability inputs for underwriting, reserving, and risk diversification workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Undisclosed helper modules may perform external lookups or downloads and persist location data in a local cache. <br>
Mitigation: Use only the documented local raster loss calculator path unless third-party geocoding, network download behavior, and persistent AOI caching are acceptable for the deployment. <br>
Risk: Credential helper code may read local secrets for services outside the advertised risk-mapping workflow. <br>
Mitigation: Review credential access before installation and avoid invoking credential helper modules unless those local secret reads are intended. <br>
Risk: Unpinned dependencies can change behavior across installations. <br>
Mitigation: Pin and review runtime dependencies before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-insurance-risk-mapping) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Analysis, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated outputs include GeoTIFF loss maps, JSON risk reports, and a JSON run manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports synthetic offline runs and local multi-band GeoTIFF inputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact metadata and changelog report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
