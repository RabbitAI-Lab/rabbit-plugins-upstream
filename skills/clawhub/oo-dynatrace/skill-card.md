## Description: <br>
Dynatrace (dynatrace.com). Use this skill for ANY Dynatrace request - searching and reading data. Whenever a task involves Dynatrace, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to inspect Dynatrace monitored entities and Problems API data through an OOMOL-connected account. It is intended for searching and reading Dynatrace data while relying on the live connector schema before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connector commands can operate in authenticated Dynatrace and OOMOL contexts, so misuse could expose operational data or affect privileged workflows. <br>
Mitigation: Install only where this access is expected, keep credentials scoped, and review commands before execution. <br>
Risk: Future or schema-discovered actions tagged as write or destructive may change or remove Dynatrace data. <br>
Mitigation: Fetch the live action schema first and require explicit user confirmation of the payload, target, and effect before any write or destructive action. <br>
Risk: Authentication, connection, or billing setup commands may open account-level workflows outside the immediate data-read request. <br>
Mitigation: Run setup steps only after a matching command failure and avoid proactively starting login, connection, or billing flows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dynatrace) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Dynatrace homepage](https://www.dynatrace.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute oo CLI connector schema and run commands that return JSON responses containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
