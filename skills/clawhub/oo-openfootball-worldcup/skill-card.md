## Description: <br>
Provides agent access to the public OpenFootball World Cup JSON dataset through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect connector schemas and query World Cup groups, teams, matches, stadiums, squads, and qualification playoff data from the public OpenFootball dataset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that fallback setup can install and authenticate the oo CLI, which is broader than the read-only dataset use case requires. <br>
Mitigation: Use an already installed and signed-in oo CLI when possible; require explicit user review before running installer or login commands. <br>
Risk: World Cup match data comes from a community dataset and is not an official real-time results source. <br>
Mitigation: Treat returned match data as community-maintained reference data and verify time-sensitive or official results against authoritative sources. <br>


## Reference(s): <br>
- [OpenFootball World Cup dataset](https://github.com/openfootball/worldcup.json) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openfootball-worldcup) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only dataset queries; connector responses include data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
