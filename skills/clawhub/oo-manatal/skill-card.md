## Description: <br>
Manatal (manatal.com). Use this skill for ANY Manatal request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiting and talent operations users use this skill to read, create, and update Manatal candidates, jobs, matches, and organizations through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create and update actions can change Manatal records. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Broad or stale Manatal credentials could expose or modify recruiting data beyond the user's intent. <br>
Mitigation: Use a limited-scope Manatal API token where possible and reconnect or refresh credentials only when an authenticated command fails. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-manatal) <br>
- [Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Manatal Homepage](https://www.manatal.com/) <br>
- [OOMOL Manatal Connection](https://console.oomol.com/app-connections?provider=manatal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns Manatal connector responses as JSON when actions run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
