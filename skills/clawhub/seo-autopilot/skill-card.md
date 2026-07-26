## Description: <br>
Run local SEO autopilot for boll-koll.se or hyresbyte.se and return a pull request link plus summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamhjort](https://clawhub.ai/user/adamhjort) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and site operators use this skill to run a local SEO automation workflow for boll-koll.se or hyresbyte.se and receive the resulting pull request link, command output, and a short SEO findings summary when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local seo-autopilot executable from PATH for the selected site. <br>
Mitigation: Install only when that executable is trusted, and prefer explicit prompts such as 'seo hyresbyte.se' when accidental default-site runs would matter. <br>


## Reference(s): <br>
- [Seo Autopilot on ClawHub](https://clawhub.ai/adamhjort/skills/seo-autopilot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary with command output and a pull request URL when produced] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs only for boll-koll.se or hyresbyte.se and may include the top three findings from SEO_REPORT.md when present.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
