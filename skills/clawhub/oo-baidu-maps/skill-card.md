## Description: <br>
Baidu Maps lets agents search and read Baidu Maps data through OOMOL's Baidu Maps connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to perform Baidu Maps search, geocoding, reverse geocoding, route planning, IP location, place lookup, administrative division queries, and weather lookup through OOMOL's connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Baidu Maps requests are mediated through OOMOL and may use a connected Baidu Maps account or API key. <br>
Mitigation: Install only if that intermediary is acceptable, and connect only the Baidu Maps account or API key intended for agent use. <br>
Risk: The skill may ask the agent to install or run the oo CLI when local setup is missing. <br>
Mitigation: Review the oo CLI install command before running it, and run setup only when authentication or connection errors require it. <br>


## Reference(s): <br>
- [Baidu Maps](https://lbsyun.baidu.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI and a connected OOMOL Baidu Maps account; action schemas are fetched before payloads are built.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
