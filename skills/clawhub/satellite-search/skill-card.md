## Description: <br>
Offline-first remote sensing satellite parameter search skill. Integrates eoPortal (ESA), WMO OSCAR, CelesTrak SATCAT, and SatNOGS DB into a local index for instant queries. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and remote-sensing practitioners use this skill to search bilingual satellite parameter indexes and retrieve merged details by satellite name or NORAD catalog number. It is especially useful when comparing parameters across eoPortal, WMO OSCAR, CelesTrak SATCAT, and SatNOGS DB. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the package ships an unrelated credential helper that can read home-directory secrets and includes a hardcoded Earthdata password. <br>
Mitigation: Audit or remove _geoskill_core/credentials.py before installation, rotate the exposed Earthdata credential, and avoid running the package where ~/.netrc or ~/.geoskill/secrets.json contains sensitive accounts unless sandboxed. <br>
Risk: The server security guidance flags ambiguous unpinned install requirements. <br>
Mitigation: Do not run pip install -r requirements.txt in a sensitive environment until dependencies are pinned or replaced with explicit local paths. <br>


## Reference(s): <br>
- [eoPortal Satellite Missions](https://www.eoportal.org/satellite-missions) <br>
- [WMO OSCAR Satellites](https://space.oscar.wmo.int/satellites) <br>
- [CelesTrak SATCAT](https://celestrak.org/pub/satcat.csv) <br>
- [SatNOGS DB Satellites API](https://db.satnogs.org/api/satellites/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON result interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline-first local index; online fetch, web search, and LLM translation paths may contact external services unless opt-out variables are set.] <br>

## Skill Version(s): <br>
0.4.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
