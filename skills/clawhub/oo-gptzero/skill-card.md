## Description: <br>
GPTZero helps an agent analyze plain text with GPTZero through OOMOL and return document-, paragraph-, and sentence-level AI-detection scores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they need an agent to check whether supplied text appears AI-generated using GPTZero. The skill guides the agent to inspect the live OOMOL connector schema, run the GPTZero detect_text action, and return document-, paragraph-, and sentence-level scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided text is sent through OOMOL to GPTZero for AI-detection analysis. <br>
Mitigation: Confirm users are comfortable using OOMOL as the intermediary and sending the text to the external GPTZero service before analysis. <br>
Risk: Setup and install commands can change the local environment or open account connection flows. <br>
Mitigation: Only run first-time setup steps when the oo CLI is missing or an authentication, connection, or billing error occurs. <br>


## Reference(s): <br>
- [ClawHub GPTZero Skill Page](https://clawhub.ai/oomol/skills/oo-gptzero) <br>
- [GPTZero Homepage](https://gptzero.me) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill fetches the live connector schema before constructing payloads and may return JSON data with execution metadata from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
