## Description: <br>
Mocean lets agents operate Mocean account workflows, including balance checks, message status checks, pricing lookups, number lookup, and SMS sending through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Mocean messaging and account actions from an agent through an OOMOL-connected Mocean account. It supports read actions for balance, message status, pricing, and number lookup, plus SMS sending after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SMS sending can contact real recipients and incur account charges. <br>
Mitigation: Confirm the exact recipient, message body, and expected effect with the user before running the write action. <br>
Risk: Mocean actions depend on a signed-in OOMOL account, an active Mocean connection, and sufficient billing credit. <br>
Mitigation: Use the documented setup and billing recovery steps only after a command fails with the matching authentication, connection, or billing error. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mocean) <br>
- [Mocean homepage](https://moceanapi.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; SMS sending requires user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
