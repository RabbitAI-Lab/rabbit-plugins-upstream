## Description: <br>
Runs geographically weighted regression with bisquare or Gaussian kernels, selects a fixed bandwidth with AICc, and writes local coefficient and local R2 outputs for spatial analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and spatial data scientists use this skill to run local spatial regression on synthetic samples or local CSV data and inspect how model coefficients and local fit vary across a geographic area. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes vendored helper modules for credentials, geocoding, downloads, caches, and remote-sensing services that are outside the advertised offline GWR workflow. <br>
Mitigation: Review or remove the unrelated vendored core before deployment, install only from a trusted publisher, and run with least privilege, no unnecessary secrets, and restricted network access when possible. <br>
Risk: Spatial results can be misleading for large or high-latitude areas because the GWR script uses Euclidean distance in degree coordinates and a proxy local R2 calculation. <br>
Mitigation: Use small, appropriate WGS84 extents, validate outputs against domain expectations, and prefer a projection-aware or great-circle implementation when distance accuracy is critical. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-geographically-weighted-regression) <br>
- [Brunsdon, Fotheringham, and Charlton 1996 DOI](https://doi.org/10.1111/j.1538-4632.1996.tb00936.x) <br>
- [Hurvich and Tsai 1989 DOI](https://doi.org/10.1093/biomet/76.2.297) <br>
- [Paez, Farber, and Wheeler 2011 DOI](https://doi.org/10.1068/b100708j) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [GeoTIFF rasters, JSON statistics and manifest files, and concise command-line text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local_coefficients.tif, local_r2.tif, gwr_stats.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and executable VERSION; changelog and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
