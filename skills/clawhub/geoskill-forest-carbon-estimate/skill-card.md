## Description: <br>
Estimate forest carbon stock from remote sensing data using BEF, allometric equations, or IPCC Tier 1/2 methods, with Monte Carlo uncertainty analysis for raster and tabular inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and forestry teams use this skill to estimate forest carbon stock from GeoTIFF, CSV, or single-point inputs and to generate uncertainty estimates for carbon reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may perform remote place or STAC lookups in the from-canopy-height workflow even though other text presents processing as local-only. <br>
Mitigation: Use the standard local input workflows for offline or sensitive-location processing, and run from-canopy-height only when remote lookups are acceptable. <br>
Risk: The from-canopy-height workflow can fall back to synthetic placeholder canopy-height data when remote data is unavailable. <br>
Mitigation: Treat placeholder-derived output as test data and require validated source rasters before using estimates for production reporting. <br>
Risk: Forest carbon estimates depend on method choice, forest type defaults, and input data quality. <br>
Mitigation: Review method, forest type, input provenance, and uncertainty intervals before using results in decisions or publications. <br>


## Reference(s): <br>
- [IPCC 2006 Guidelines for National Greenhouse Gas Inventories](https://www.ipcc-nggip.iges.or.jp/public/2006gl/) <br>
- [IPCC 2019 Refinement to the 2006 Guidelines](https://www.ipcc-nggip.iges.or.jp/public/2019rf/) <br>
- [Global Forest Watch](https://www.globalforestwatch.org/) <br>
- [NASA GEDI](https://gedi.umd.edu/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples, JSON summaries, CSV tables, and GeoTIFF output paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce carbon stock estimates, uncertainty intervals, QA summaries, CSV reports, and GeoTIFF rasters depending on the selected workflow.] <br>

## Skill Version(s): <br>
4.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
