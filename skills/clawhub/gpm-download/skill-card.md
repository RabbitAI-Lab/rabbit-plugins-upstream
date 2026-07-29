## Description: <br>
Downloads GPM IMERG precipitation data from NASA GES DISC and helps agents search, download, and summarize HDF5 precipitation files by date range, bounding box, and variable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and data analysts use this skill to automate discovery and download of NASA GPM IMERG precipitation data for hydrology, climate, agriculture, and geospatial workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Undeclared shared credentials may expose or reuse credentials that do not belong to the installing user. <br>
Mitigation: Remove embedded credentials, rotate any exposed credentials, and require users to provide their own credentials through documented opt-in configuration. <br>
Risk: Credential helpers may read local credential files or home-directory secret files even though the skill claims no credentials are used. <br>
Mitigation: Run the skill in a sandbox or clean HOME, review credential-file access before installation, and disable local credential reads unless explicitly needed. <br>
Risk: Optional geocoding and cache behavior can send place queries to external services and store derived data in the user's home directory. <br>
Mitigation: Prefer explicit bounding boxes for sensitive work, allowlist expected endpoints, and document or disable home-directory caching unless the user opts in. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/gpm-download) <br>
- [NASA GES DISC](https://disc.gsfc.nasa.gov/) <br>
- [GPM IMERG Late Run archive pattern](https://gpmweb2.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDL.07/YYYY/MM/) <br>
- [README.md](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Files] <br>
**Output Format:** [Markdown guidance with shell commands; the CLI can emit text or JSON and download HDF5 data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads are written to a local output directory; optional CSV summaries may be generated from downloaded HDF5 files.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
