## Description: <br>
CLI for AI agents to lookup SpaceX launches and rockets for their humans. No auth required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use this skill to answer SpaceX launch, rocket, and crew questions from public SpaceX API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed bundle does not include the actual CLI script, so executable code may differ from the reviewed documentation. <br>
Mitigation: Inspect and pin the external repository before running the CLI in an agent environment. <br>
Risk: Community-maintained SpaceX API data may lag behind real-time launch changes. <br>
Mitigation: Verify time-sensitive launch information with an authoritative source before relying on it for operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jeffaf/skills/spacex) <br>
- [SpaceX API](https://github.com/r-spacex/SpaceX-API) <br>
- [SpaceX API Documentation](https://github.com/r-spacex/SpaceX-API/tree/master/docs) <br>
- [SpaceX API v4 base URL](https://api.spacexdata.com/v4) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text and markdown with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, and jq; uses public SpaceX API data without authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
