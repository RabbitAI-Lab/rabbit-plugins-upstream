## Description: <br>
GutCheck - A digestive health tracking application with personalized insights and data-driven recommendations. Helps users understand food sensitivities and optimize gut wellness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[allen566](https://clawhub.ai/user/allen566) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users install this skill to set up and run GutCheck, a Node-based digestive health tracker for logging meals, tracking digestive responses, and viewing personalized food-sensitivity and gut-wellness insights. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and runs a Node application from an external GitHub repository. <br>
Mitigation: Review the repository and dependency tree before installation, and run it in a local or test environment first. <br>
Risk: The app may handle sensitive digestive-health and food-response information. <br>
Mitigation: Avoid entering sensitive health details until you have reviewed the app's privacy behavior and storage configuration. <br>
Risk: Weak local configuration could expose accounts or session tokens. <br>
Mitigation: Use a local or test database and set a strong JWT secret before running the app. <br>
Risk: The artifact includes a publishing script and ClawHub publish commands. <br>
Mitigation: Do not run publishing commands unless you intentionally want to publish the skill from your own account. <br>


## Reference(s): <br>
- [GutCheck ClawHub listing](https://clawhub.ai/allen566/skills/gutcheck) <br>
- [GutCheck source repository](https://github.com/openclaw/gutcheck.git) <br>
- [Publisher profile](https://clawhub.ai/user/allen566) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with shell commands and environment configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm; the installed app uses Express, MongoDB via mongoose, bcrypt, jsonwebtoken, cors, and dotenv.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
