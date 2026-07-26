## Description: <br>
Consulta y optimiza precios de electricidad PVPC en España para la tarifa doméstica 2.0TD, including current price context, tariff periods, cheap-hour ranges, and appliance scheduling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[didelco](https://clawhub.ai/user/didelco) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to check Spanish PVPC electricity prices, understand the current 2.0TD tariff period, find cheaper hours, and schedule household appliances to reduce electricity cost. <br>

### Deployment Geography for Use: <br>
Spain <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes online requests to the public ESIOS/REE API, so results may be unavailable or stale if the API cannot be reached or has not published the latest prices. <br>
Mitigation: Confirm time-sensitive pricing before acting on cost-sensitive recommendations, and handle script errors as unavailable data rather than advice. <br>
Risk: Holiday tariff-period recommendations may be inaccurate because the skill treats national holidays as weekdays. <br>
Mitigation: Check Spanish public holidays separately before relying on valley, flat, or peak period guidance for holiday dates. <br>


## Reference(s): <br>
- [ESIOS public PVPC JSON API](https://api.esios.ree.es/archives/70/download_json?locale=es&date={date_str}) <br>
- [ClawHub skill page](https://clawhub.ai/didelco/skills/pvpc-spain) <br>
- [Publisher profile](https://clawhub.ai/user/didelco) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text or JSON from local Python scripts, often accompanied by concise markdown guidance from the agent.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on live public ESIOS/REE API availability and the requested script options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
