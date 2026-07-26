## Description: <br>
Helps agents operate PartnerStack through an OOMOL-connected account by inspecting live connector schemas and running read/list or customer-creation actions with the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve PartnerStack customers, partnerships, deals, and leads, and to create PartnerStack customers after confirming the payload. It is intended for agents operating through an already connected OOMOL account rather than direct PartnerStack API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing customer creation can modify PartnerStack data when a payload is wrong or unintended. <br>
Mitigation: Confirm the exact create_customer payload and expected effect with the user before running the write action. <br>
Risk: The skill depends on an OOMOL-brokered PartnerStack connection and the oo CLI installation/authentication path. <br>
Mitigation: Install and authenticate only after trusting OOMOL, and treat CLI installation and account connection as separate trust decisions. <br>
Risk: Expired credentials, missing scopes, unavailable app connections, or billing stops can block connector execution. <br>
Mitigation: Resolve connection, scope, credential, and billing failures through the documented OOMOL console paths before retrying. <br>


## Reference(s): <br>
- [PartnerStack homepage](https://partnerstack.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [OOMOL PartnerStack connection](https://console.oomol.com/app-connections?provider=partnerstack) <br>
- [ClawHub PartnerStack skill page](https://clawhub.ai/oomol/skills/oo-partnerstack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
