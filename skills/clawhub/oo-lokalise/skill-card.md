## Description: <br>
Lokalise helps an agent read, create, update, and delete Lokalise projects, languages, keys, and translations through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and localization operators use this skill to inspect Lokalise projects, languages, keys, and translations, and to create, update, or delete localization records through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Lokalise keys or translations in the connected account. <br>
Mitigation: Review the project, target record, payload, and intended effect before approving create or update commands. <br>
Risk: The destructive delete action can remove a Lokalise key. <br>
Mitigation: Require explicit user approval for the exact key and project before running a destructive command. <br>
Risk: Account connection or billing issues can prevent connector actions from completing. <br>
Mitigation: Use the first-time setup and billing guidance only after a command fails with the matching error. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lokalise) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Lokalise homepage](https://lokalise.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and execution metadata when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
