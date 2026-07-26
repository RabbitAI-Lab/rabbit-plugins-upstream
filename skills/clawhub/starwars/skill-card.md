## Description: <br>
CLI for AI agents to lookup Star Wars universe info for their humans. Uses SWAPI. No auth required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to answer Star Wars lookup requests by querying characters, planets, films, species, and starships through SWAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lookup terms are sent to swapi.dev when the skill queries Star Wars data. <br>
Mitigation: Use the skill for ordinary Star Wars lookup terms and avoid sending sensitive or private text as search input. <br>
Risk: Manual installation instructions reference cloning an external repository and creating executable or system path links. <br>
Mitigation: Prefer the ClawHub install path when available, and inspect the external repository and shell commands before running manual installation steps. <br>
Risk: SWAPI coverage is limited to original and prequel film data, so sequel trilogy, TV, and extended-universe answers may be incomplete. <br>
Mitigation: Treat results as scoped to SWAPI coverage and use another source when the user asks about unsupported Star Wars material. <br>


## Reference(s): <br>
- [SWAPI - Star Wars API](https://swapi.dev) <br>
- [ClawHub skill page](https://clawhub.ai/jeffaf/skills/starwars) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text CLI output with concise lookup summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, and jq; sends lookup terms to swapi.dev.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
