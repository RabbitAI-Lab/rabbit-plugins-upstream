## Description: <br>
Locally evaluates password strength by length, character variety, entropy, and common weaknesses, then returns a 0-100 score with improvement suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freedompixels](https://clawhub.ai/user/freedompixels) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security educators, and account administrators use this skill to run local password-strength checks and explain concrete improvements before passwords are used or shared with users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaintext passwords can appear in shell history, terminal output, CI logs, recorded sessions, or monitored environments when users pass real passwords on the command line or use batch mode. <br>
Mitigation: Run the skill only in local private terminals, avoid real passwords in shared or recorded environments, and protect or disable histories and logs when testing sensitive values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/freedompixels/skills/cn-password-strength) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and plaintext terminal output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-only Python standard library utility; batch mode can print plaintext passwords.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
