## Description: <br>
CLI for AI agents to look up Pokemon information using PokeAPI without authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users can use this skill to let an agent answer Pokemon lookup questions, including searches, stats, type matchups, and ability details from PokeAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed package contains documentation while the README references executable wrapper and script files from the installed repository. <br>
Mitigation: Before relying on the skill, verify that the installed repository contains the expected pokemon wrapper and scripts and scan those files. <br>
Risk: The skill depends on live PokeAPI responses for lookup accuracy and availability. <br>
Mitigation: Treat results as external API data and retry or cross-check if PokeAPI is unavailable or returns unexpected content. <br>


## Reference(s): <br>
- [ClawHub Pokemon skill page](https://clawhub.ai/jeffaf/skills/pokemon) <br>
- [PokeAPI](https://pokeapi.co) <br>
- [PokeAPI v2 documentation](https://pokeapi.co/docs/v2) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text summaries and tables with Markdown command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, and jq; makes read-only requests to PokeAPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
