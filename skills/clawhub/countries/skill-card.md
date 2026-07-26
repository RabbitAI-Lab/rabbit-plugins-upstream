## Description: <br>
CLI for AI agents to lookup country info for their humans. Uses REST Countries API. No auth required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill through an agent to answer country lookup questions by name, country code, capital city, or region using REST Countries API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Country lookup terms are sent to restcountries.com. <br>
Mitigation: Use non-sensitive country names, codes, capitals, or regions, and avoid private free-form text in search queries. <br>
Risk: Installation examples reference an external GitHub CLI. <br>
Mitigation: Verify the external repository and file contents before cloning or symlinking the CLI into an agent PATH. <br>
Risk: Broad invocation wording may route non-country questions to this skill. <br>
Mitigation: Use the documented command patterns for country names, country codes, capital cities, and supported regions. <br>


## Reference(s): <br>
- [Countries ClawHub skill page](https://clawhub.ai/jeffaf/skills/countries) <br>
- [REST Countries API](https://restcountries.com) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text CLI output with Markdown usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, jq, and bc; no API key is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
