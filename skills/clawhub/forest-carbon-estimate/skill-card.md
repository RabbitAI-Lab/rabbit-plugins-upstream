## Description: <br>
Estimates forest carbon stock from remote sensing or tabular inputs using BEF, allometric, and IPCC Tier 1/2 methods with optional Monte Carlo uncertainty analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and environmental teams use this skill to run forest carbon estimates from GeoTIFF rasters, CSV plot data, or single-point inputs and produce maps, reports, or uncertainty summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-name and from-canopy-height workflows may send location queries or AOIs to external geocoding and STAC services. <br>
Mitigation: Use local GeoTIFF or CSV inputs, or review the external services involved before running place-based workflows when location privacy matters. <br>
Risk: User-selected output paths can overwrite or replace local files. <br>
Mitigation: Write outputs to a dedicated working directory and confirm filenames before running commands that create GeoTIFF, CSV, or JSON files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/forest-carbon-estimate) <br>
- [Detailed method notes](references/details.md) <br>
- [IPCC 2006 Guidelines](https://www.ipcc-nggip.iges.or.jp/public/2006gl/) <br>
- [IPCC 2019 Refinement](https://www.ipcc-nggip.iges.or.jp/public/2019rf/) <br>
- [Global Forest Watch](https://www.globalforestwatch.org/) <br>
- [NASA GEDI](https://gedi.umd.edu/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated files may include GeoTIFF, CSV, and JSON outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local raster and tabular workflows plus optional place-based workflows that may contact external geocoding or STAC services.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
