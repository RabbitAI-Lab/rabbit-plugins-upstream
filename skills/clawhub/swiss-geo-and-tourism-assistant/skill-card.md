## Description: <br>
Helps agents answer Switzerland-focused geodata, tourism, transit, POI, weather, hazard, elevation, coordinate, and map-link questions using disclosed public data sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mbjoern](https://clawhub.ai/user/mbjoern) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, travel planners, and agents use this skill to look up Swiss places, addresses, elevation, public transport options, map layers, POIs, and tourism context. It is most useful for Swiss trip planning, local orientation, and geography questions that benefit from official map links or public open-data lookups. <br>

### Deployment Geography for Use: <br>
Global use for Switzerland-focused geodata and tourism queries. <br>

## Known Risks and Mitigations: <br>
Risk: Swiss weather, avalanche, flood, hiking, and natural-hazard information can be safety-critical or time-sensitive. <br>
Mitigation: Verify safety-critical outputs against official sources before relying on them for travel, hiking, or emergency decisions. <br>
Risk: Location queries, private addresses, and detailed travel plans may be sent to the disclosed external public APIs used by the skill. <br>
Mitigation: Avoid entering sensitive private addresses or detailed personal itineraries unless sharing them with those APIs is acceptable. <br>
Risk: The optional MySwitzerland API flow requires an API key. <br>
Mitigation: Use the MYSWITZERLAND_API_KEY environment variable and avoid pasting secrets into prompts, chat transcripts, or generated examples. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/mbjoern/skills/swiss-geo-and-tourism-assistant) <br>
- [Swisstopo API Referenz](references/api.md) <br>
- [geo.admin.ch API](https://api3.geo.admin.ch/) <br>
- [geo.admin.ch map viewer](https://map.geo.admin.ch/) <br>
- [transport.opendata.ch API](https://transport.opendata.ch/) <br>
- [MeteoSwiss Open Data](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html) <br>
- [SLF avalanche bulletin](https://www.slf.ch/de/lawinenbulletin-und-schneesituation.html) <br>
- [BAFU hydrological data](https://www.hydrodaten.admin.ch/de/aktuelle-lage) <br>
- [opentransportdata.swiss](https://opentransportdata.swiss/) <br>
- [opendata.swiss](https://opendata.swiss/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown responses with API URLs, map links, concise explanations, and optional shell command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live lookup guidance, public API examples, generated geo.admin.ch links, POI summaries, transit schedule summaries, and notes when MySwitzerland API use requires MYSWITZERLAND_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
