## Description: <br>
Supervisely (supervisely.com). Use this skill for ANY Supervisely request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect live Supervisely connector schemas and run read-oriented Supervisely actions through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose Supervisely data available to the connected OOMOL account. <br>
Mitigation: Review the OOMOL connection and Supervisely API-key scopes before installation and use. <br>
Risk: The first-time setup path includes remote installer and account sign-in commands. <br>
Mitigation: Run setup only when the CLI, authentication, or connection is missing, and treat those steps as sensitive account setup. <br>
Risk: Incorrect action payloads can cause failed or unintended connector calls. <br>
Mitigation: Inspect the live connector schema for each action before constructing the JSON payload. <br>


## Reference(s): <br>
- [Supervisely homepage](https://supervisely.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-supervisely) <br>
- [OOMOL ClawHub profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
