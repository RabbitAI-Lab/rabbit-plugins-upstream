## Description: <br>
browser-cli-tool-free guides agents in using the agent-browser CLI to navigate web pages, interact with elements, extract page information, and capture screenshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate browser pages for personal check-ins, form filling, page inspection, screenshots, and light web data collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can interact with sensitive logged-in pages and capture sensitive page content in screenshots. <br>
Mitigation: Review each browser command before execution, avoid sensitive sessions unless necessary, and manage screenshot files as potentially sensitive local artifacts. <br>
Risk: Recurring unattended web actions can submit forms or perform sign-ins without enough oversight. <br>
Mitigation: Require explicit confirmation before automating submissions, sign-ins, or scheduled tasks, and confirm that the target site's rules allow the automation. <br>
Risk: The security summary notes a mismatch between generic trigger text and the skill's real browser-control behavior. <br>
Mitigation: Use the skill only for intentional browser-control tasks such as navigation, interaction, extraction, and screenshots. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/browser-cli-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with bash command examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+, agent-browser CLI, and Chromium; may create screenshots or scheduled shell scripts when invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
