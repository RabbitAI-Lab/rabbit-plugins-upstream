## Description: <br>
Estimate forest carbon stock from remote sensing data using BEF, allometric equations, or IPCC Tier 1/2 methods, with Monte Carlo uncertainty analysis for raster and tabular inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and forestry teams use this skill to estimate forest carbon stock from height, biomass, GeoTIFF, or CSV inputs and to produce uncertainty summaries for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security review flagged under-disclosed network behavior in geocoding, STAC, and related helper paths. <br>
Mitigation: Run only in environments where external geocoding and STAC requests are acceptable, and avoid network-enabled commands such as from-canopy-height unless that data sharing is approved. <br>
Risk: Security review reported bundled credential-handling code with hardcoded Earthdata credential defaults. <br>
Mitigation: Remove or replace bundled credential defaults before use, rely on user-managed environment variables or secret stores, and rotate any exposed credentials. <br>
Risk: Security review found that the local-only privacy statement does not match all available behavior. <br>
Mitigation: Treat privacy claims as unverified for network-enabled workflows and document any external service calls before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/forest-carbon-estimate) <br>
- [IPCC 2006 Guidelines for National Greenhouse Gas Inventories](https://www.ipcc-nggip.iges.or.jp/public/2006gl/) <br>
- [IPCC 2019 Refinement to the 2006 Guidelines](https://www.ipcc-nggip.iges.or.jp/public/2019rf/) <br>
- [Global Forest Watch](https://www.globalforestwatch.org/) <br>
- [NASA GEDI](https://gedi.umd.edu/) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated tool outputs may include JSON, CSV, and GeoTIFF files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce carbon stock estimates, uncertainty statistics, raster outputs, CSV summaries, and QA JSON depending on command options.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
