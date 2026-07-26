## Description: <br>
Download GPM IMERG precipitation data from NASA GES DISC at 0.1 degree resolution, with search, download, JSON, QA, and optional CSV summary outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers use this skill to locate and download NASA GPM IMERG precipitation files for a date range, variables, and geographic area. It can emit machine-readable search and QA summaries and save downloaded HDF5 data for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using --place may send location names to third-party geocoders and cache resolved locations under ~/.geoskill_core_cache. <br>
Mitigation: Use explicit --bbox coordinates when location privacy matters and review or clear the local geocoding cache before broad deployment. <br>
Risk: The public privacy disclosure emphasizes NASA-only requests and can understate --place behavior. <br>
Mitigation: Update deployment guidance so users understand when third-party geocoding is used and when --bbox avoids it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/gpm-download) <br>
- [NASA GES DISC](https://disc.gsfc.nasa.gov/) <br>
- [GPM IMERG Late Run data endpoint](https://gpmweb2.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDL.07/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, files, shell commands, configuration] <br>
**Output Format:** [Plain text or JSON CLI output, downloaded HDF5 files, optional QA JSON, and optional CSV summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads are written to a local output directory; --qa implies download and writes a JSON summary.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
