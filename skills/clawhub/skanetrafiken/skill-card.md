## Description: <br>
Skåne public transport trip planner (Skånetrafiken). Plans bus/train journeys with real-time delays. Supports stations, addresses, landmarks, and cross-border trips to Copenhagen. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rezkam](https://clawhub.ai/user/rezkam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to search Skånetrafiken locations, disambiguate stops, addresses, or landmarks, and plan public transport trips in Skåne with real-time timing, disruption, walking, and platform details. <br>

### Deployment Geography for Use: <br>
Sweden and Denmark cross-border routes served by Skånetrafiken <br>

## Known Risks and Mitigations: <br>
Risk: Location searches and journey planning send searched locations, coordinates, and intended travel times to Skånetrafiken. <br>
Mitigation: Install only from trusted sources and avoid entering exact home, work, or sensitive addresses unless that privacy tradeoff is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rezkam/skills/skanetrafiken) <br>
- [Skånetrafiken Points API](https://www.skanetrafiken.se/gw-tps/api/v2/Points) <br>
- [Skånetrafiken Journey API](https://www.skanetrafiken.se/gw-tps/api/v2/Journey) <br>
- [Agent Skills](https://agentskills.io) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and formatted trip results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; scripts query Skånetrafiken for location search and journey planning.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
