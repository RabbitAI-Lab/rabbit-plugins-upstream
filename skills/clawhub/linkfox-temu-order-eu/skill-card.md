## Description: <br>
This skill helps agents work with Temu EU order-management APIs through the LinkFox gateway, including order lists and details, shipping information, order amounts, combined shipments, customization records, and SN/IMEI verification upload. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to query and manage authorized Temu Europe order data, inspect shipping and amount records, retrieve customization data, and upload serial-number or IMEI verification details. <br>

### Deployment Geography for Use: <br>
Global use for authorized Temu EU order operations <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive customer order records, including decrypted addresses and SN/IMEI data. <br>
Mitigation: Use it only for authorized Temu EU order operations in trusted workspaces, and delete archived LinkFox response files when they are no longer needed. <br>
Risk: Reusable Temu access tokens may be stored locally in plaintext by the bundled token store. <br>
Mitigation: Avoid storing production tokens unless plaintext local credential persistence is acceptable, and prefer short-lived or tightly scoped credentials where possible. <br>
Risk: Unmasked token listing or copied command input can expose credentials. <br>
Mitigation: Avoid sharing terminal output or saved token files, and review token displays before pasting logs into other tools. <br>


## Reference(s): <br>
- [API reference](references/api.md) <br>
- [Temu access token guide](references/access-token.md) <br>
- [Authorization flow](references/authorization-flow.md) <br>
- [Partner EU order catalog](references/partner-eu-catalog.md) <br>
- [Per-interface API documents](references/apis/README.md) <br>
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Files] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Large API responses are summarized on stdout while full JSON responses are written under the current workspace.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
