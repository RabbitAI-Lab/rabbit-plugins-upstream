## Description: <br>
CLI for AI agents to find recipes for their humans using TheMealDB API without authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to search for recipes, retrieve full meal details, get random dinner ideas, list categories, and browse meals by cuisine. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed bundle references installation and execution of CLI code from outside the reviewed package. <br>
Mitigation: Inspect the referenced repository and scripts before use, avoid elevated privileges, and prefer a release that includes or pins the executable code. <br>


## Reference(s): <br>
- [Recipes skill on ClawHub](https://clawhub.ai/jeffaf/skills/recipes) <br>
- [TheMealDB](https://www.themealdb.com) <br>
- [TheMealDB API](https://www.themealdb.com/api.php) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [CLI text output with recipe IDs, ingredients, instructions, and source or video links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, and jq; uses TheMealDB without an API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
