## Description: <br>
satellite_search is an offline-first Chinese-language satellite parameter lookup skill that combines eoPortal, WMO OSCAR, CelesTrak SATCAT, and SatNOGS data into a local index, with optional online fetch, web-search fallback, and LLM translation paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and remote-sensing practitioners use this skill to search satellite names or NORAD IDs and retrieve merged satellite metadata, orbital parameters, source URLs, and bilingual summaries from local and optional online sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes an unrelated ClawHub publishing script and may read a publishing token if run intentionally. <br>
Mitigation: Review the package before installation, do not run publish_to_clawhub.py, and do not expose CLAWHUB_TOKEN unless publishing to ClawHub is intended. <br>
Risk: Ambiguous dependency entries in requirements.txt can make installation behavior harder to review. <br>
Mitigation: Pin and clean up dependencies before deploying the skill in a managed environment. <br>
Risk: Missed local queries can be sent to external search engines through the online fallback. <br>
Mitigation: Set SATELLITE_SEARCH_NO_ONLINE=1 when external search requests are not acceptable. <br>
Risk: The translate command can send eoPortal text to the configured LLM endpoint. <br>
Mitigation: Set SATELLITE_SEARCH_NO_LLM=1 when LLM translation traffic is not acceptable, and review OPENAI_API_KEY and OPENAI_BASE_URL handling before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/satellite-search) <br>
- [eoPortal satellite missions](https://www.eoportal.org/satellite-missions) <br>
- [WMO OSCAR satellites](https://space.oscar.wmo.int/satellites) <br>
- [CelesTrak SATCAT CSV](https://celestrak.org/pub/satcat.csv) <br>
- [SatNOGS satellite API](https://db.satnogs.org/api/satellites/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON-shaped satellite lookup results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include bilingual Chinese and English summaries, source URLs, orbital metadata, and privacy-relevant notes for optional online search or LLM translation.] <br>

## Skill Version(s): <br>
0.4.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
