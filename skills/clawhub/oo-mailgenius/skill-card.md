## Description: <br>
MailGenius lets agents read, create, and update MailGenius data through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage MailGenius deliverability audit workflows through an OOMOL-connected account, including creating test email audits and checking audit results, daily limits, and generated test email records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The create_email_audit action changes MailGenius state by generating a test email address. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Setup and account connection commands can affect local CLI state or start account workflows. <br>
Mitigation: Run installation, login, or connection steps only after a command reports missing setup or authorization. <br>


## Reference(s): <br>
- [MailGenius homepage](https://www.mailgenius.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailgenius) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, json] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
