## Description: <br>
Offline-first remote sensing satellite parameter search skill that integrates eoPortal, WMO OSCAR, CelesTrak SATCAT, and SatNOGS DB into a local index for satellite queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, remote sensing analysts, and researchers use this skill to query satellite parameters by name or NORAD ID from a bundled local index and, when enabled, refresh or fetch public source records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is network-capable and can scrape public sites, send missed queries to search engines, and optionally send eoPortal text to an LLM provider. <br>
Mitigation: Review outbound destinations before use and set SATELLITE_SEARCH_NO_ONLINE=1 or SATELLITE_SEARCH_NO_LLM=1 when those behaviors are not acceptable. <br>
Risk: The security review flags under-disclosed credential-handling code and risky dependency declarations. <br>
Mitigation: Review or remove the bundled credential module and inspect requirements.txt before installing dependencies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-satellite-search) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [eoPortal satellite missions](https://www.eoportal.org/satellite-missions) <br>
- [WMO OSCAR satellites](https://space.oscar.wmo.int/satellites) <br>
- [CelesTrak SATCAT](https://celestrak.org/pub/satcat.csv) <br>
- [SatNOGS DB satellites API](https://db.satnogs.org/api/satellites/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON satellite query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include source URLs, bilingual satellite fields, local-index search results, and opt-out configuration guidance.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
