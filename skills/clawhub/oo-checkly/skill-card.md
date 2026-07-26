## Description: <br>
Checkly (checklyhq.com). Use this skill for ANY Checkly request - searching and reading data. Whenever a task involves Checkly, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Checkly checks, check results, check statuses, and the connected Checkly account through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on OOMOL to broker the connected Checkly account. <br>
Mitigation: Install only when OOMOL is trusted to broker the Checkly connection. <br>
Risk: Future connector actions could write, delete, overwrite, or otherwise change Checkly state. <br>
Mitigation: Require explicit user approval before running any future action that changes Checkly state. <br>


## Reference(s): <br>
- [Checkly homepage](https://www.checklyhq.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Checkly skill on ClawHub](https://clawhub.ai/oomol/skills/oo-checkly) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
