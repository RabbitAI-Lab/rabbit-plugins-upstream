## Description: <br>
Compute carbon stock changes, emissions/removals, and uncertainty from multi-temporal land cover data using IPCC Tier 1/2 carbon factors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to compute land-cover transition matrices, carbon stock changes, CO2e emissions/removals, uncertainty estimates, and carbon accounting output files from before/after land-cover rasters or bounded demo runs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make optional outbound requests to download imagery and cache local files. <br>
Mitigation: Install only where outbound access to Microsoft Planetary Computer and local downloaded imagery/cache files are acceptable; pin dependencies and review or disable auto-download behavior for production workflows. <br>
Risk: Synthetic demo mode can produce real-looking carbon accounting outputs without user-supplied land-cover inputs. <br>
Mitigation: Require explicit before/after land-cover inputs for decision-making, reporting, or production carbon accounting, and label synthetic outputs as demonstrations. <br>
Risk: Tier 1/2 default carbon factors and regional averages may be unsuitable for certified MRV, VERRA, Gold Standard, or other formal reporting. <br>
Mitigation: Use locally calibrated or nationally approved factors and have qualified carbon-accounting reviewers validate assumptions before using outputs in formal reports. <br>


## Reference(s): <br>
- [Default carbon factors registry](references/carbon_factors.json) <br>
- [ClawHub skill release page](https://clawhub.ai/ruiduobao/skills/geoskill-land-use-carbon-accounting) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and generated CSV, JSON, GeoTIFF, NumPy, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces transition matrices, carbon change rasters, uncertainty summaries, request metadata, dataset manifests, output manifests, QA results, and run logs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
