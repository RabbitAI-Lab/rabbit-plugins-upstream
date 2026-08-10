## Description: <br>
Download daily GPM IMERG Late Run global precipitation data at 0.1° resolution from NASA GES DISC without authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to search for and download NASA GPM IMERG precipitation data for a date range, area of interest, and selected precipitation variables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled credential helper includes real-looking hardcoded Earthdata credentials and can read local secrets or netrc data, while the main skill description says no credentials are required. <br>
Mitigation: Remove the unused credential helper or hardcoded defaults, disclose any local credential lookup, and review the package before installation. <br>
Risk: The skill downloads remote NASA data and writes local HDF5 or CSV outputs. <br>
Mitigation: Review requested date ranges, variables, and output directories before execution, and limit downloads to expected public NASA GPM endpoints. <br>


## Reference(s): <br>
- [NASA GES DISC](https://disc.gsfc.nasa.gov/) <br>
- [GPM_3IMERGDL data endpoint pattern](https://gpmweb2.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDL.07/YYYY/MM/) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files, shell commands, guidance] <br>
**Output Format:** [CLI text or JSON summaries, downloaded HDF5 files, and optional CSV summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes NASA GPM HDF5 files to a local output directory and can export zonal-mean CSV summaries.] <br>

## Skill Version(s): <br>
5.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
