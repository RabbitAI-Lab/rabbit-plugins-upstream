## Description: <br>
Provides LinkFox gateway guidance, scripts, and API references for Temu US order management tasks including order lists, details, shipping information, order amounts, combined shipments, customizations, and SN or IMEI verification uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu sellers, operators, and developers use this skill to query and process Temu US order data through LinkFox, including shipping details, order amounts, combined shipment candidates, customization content, and verification uploads. It is intended for order and fulfillment workflows that need guided API calls or runnable helper scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Temu seller and order APIs through LinkFox and may handle sensitive order or shipping data. <br>
Mitigation: Use only the minimum required LinkFox and Temu credentials, prefer short-lived tokens when possible, and run the skill only in trusted workspaces. <br>
Risk: The artifact stores full order responses locally and can store plaintext Temu tokens. <br>
Mitigation: Avoid inline output for sensitive responses, restrict access to the working directory and the ~/.linkfox token store, and inspect or clean saved response files after use. <br>
Risk: Generic proxy utilities allow broader Temu API access than the named order workflow scripts. <br>
Mitigation: Prefer the specific us_order_* scripts for normal order workflows and use the generic proxy only when broad Temu API access is intentional. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-us) <br>
- [API Reference](references/api.md) <br>
- [Temu Access Token Guide](references/access-token.md) <br>
- [Partner US Catalog](references/partner-us-catalog.md) <br>
- [Per-Interface API References](references/apis/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API examples; scripts may emit JSON summaries or saved JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write complete responses under a local linkfox output directory and may print full responses to stdout for small responses or when inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
