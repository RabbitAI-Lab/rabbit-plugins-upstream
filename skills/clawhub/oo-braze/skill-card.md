## Description: <br>
Braze skill for searching and reading Braze campaign and Canvas data through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users who operate Braze through OOMOL-connected accounts use this skill to list and inspect campaigns and Canvases without handling raw Braze credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill brokers Braze access through OOMOL, so users rely on OOMOL for credential handling and connector execution. <br>
Mitigation: Install only when OOMOL is an approved broker for the user's Braze account and intended read workflows. <br>
Risk: Broad wording could lead an agent to attempt actions beyond the listed read-only campaign and Canvas operations. <br>
Mitigation: Before approving any unlisted action, require the exact action name, payload, and expected effect. <br>
Risk: Connector schemas may change after release. <br>
Mitigation: Inspect the live connector schema before constructing or running each payload. <br>


## Reference(s): <br>
- [Braze homepage](https://www.braze.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL Braze connection](https://console.oomol.com/app-connections?provider=braze) <br>
- [ClawHub Braze skill](https://clawhub.ai/oomol/skills/oo-braze) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; connector responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
