## Description: <br>
LeadMagic lets an agent search and read LeadMagic data through the OOMOL oo CLI connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, growth, and revenue operations users can ask an agent to enrich company and professional profiles, find work emails or mobile numbers, validate email deliverability, and check LeadMagic credits through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can request business and personal lead data, including work emails and mobile phone numbers. <br>
Mitigation: Use it only for authorized LeadMagic workflows, minimize submitted identifiers, and review returned contact data before use or sharing. <br>
Risk: First-time use may require installing the oo CLI and connecting an OOMOL account to LeadMagic. <br>
Mitigation: Review the oo CLI install command and confirm the intended OOMOL account connection before running setup. <br>
Risk: Connector actions depend on live LeadMagic schemas and account scopes. <br>
Mitigation: Fetch the action schema with oo before constructing each payload and resolve missing scopes or expired credentials through the OOMOL connection page. <br>


## Reference(s): <br>
- [LeadMagic homepage](https://leadmagic.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub LeadMagic skill page](https://clawhub.ai/oomol/skills/oo-leadmagic) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before action execution and relies on server-side OOMOL credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
