## Description: <br>
Estimates regional evapotranspiration in mm/day using Priestley-Taylor or simplified SEBAL methods from net radiation, air temperature, land surface temperature, and NDVI inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and water-resource practitioners use this skill to estimate regional evapotranspiration for irrigation demand assessment, watershed water-consumption analysis, drought monitoring, and land-surface process validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package advertises offline local computation but includes network, caching, and credential-handling utilities beyond the main evapotranspiration workflow. <br>
Mitigation: Review and trim or disable geocoding, downloader, credential, hardcoded credential, and home-directory cache behavior before use with sensitive locations or credentials. <br>
Risk: Dependencies are not pinned in requirements.txt. <br>
Mitigation: Pin and scan dependencies in a controlled environment before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-evapotranspiration-estimation) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Geospatial raster] <br>
**Output Format:** [GeoTIFF raster plus JSON statistics and run manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs ET in mm/day using EPSG:4326; supports Priestley-Taylor and simplified SEBAL methods.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
