## Description: <br>
Taggun helps agents operate Taggun through an OOMOL-connected account for receipt and invoice extraction, campaign lookup, and receipt URL validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when an agent needs to extract receipt or invoice data from public HTTPS file URLs, list Taggun campaign IDs, inspect campaign settings, or validate receipt URLs through a connected Taggun account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through OOMOL as the broker for a connected Taggun account. <br>
Mitigation: Install only when the user is comfortable using OOMOL for Taggun account access and keep credential setup limited to the documented connection flow. <br>
Risk: Receipts and invoices can contain sensitive personal, financial, or business information. <br>
Mitigation: Submit only public HTTPS file URLs that the user intends to process with Taggun, and avoid sending unrelated or private documents. <br>
Risk: Unnecessary setup commands could trigger sign-in, installation, or account-connection flows. <br>
Mitigation: Run oo CLI install, login, or connection steps only when an action fails with the matching missing-command, authentication, or connection error. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-taggun) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Taggun Homepage](https://www.taggun.io/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schema checks before action execution so payloads match the current Taggun connector contract.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence metadata and release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
