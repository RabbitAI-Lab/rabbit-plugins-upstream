## Description: <br>
CLI for AI agents to find breweries for their humans. Uses Open Brewery DB. No auth required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to search for breweries by name, city, state, type, or random suggestion using Open Brewery DB. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes public Open Brewery DB requests for brewery-related questions. <br>
Mitigation: Avoid using sensitive or private search terms and review whether public API requests are acceptable for the user's environment. <br>
Risk: The reviewed artifact does not include the executable scripts referenced by the README installation steps. <br>
Mitigation: Inspect cloned scripts before making them executable or running them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jeffaf/skills/breweries) <br>
- [Open Brewery DB](https://www.openbrewerydb.org) <br>
- [Open Brewery DB API v1](https://api.openbrewerydb.org/v1/breweries) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands] <br>
**Output Format:** [Plain text brewery lookup results with command-line examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns up to 10 results per query; requires bash, curl, and jq.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
