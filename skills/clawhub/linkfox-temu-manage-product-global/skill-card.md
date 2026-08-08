## Description:

Temu Global product management skill that uses the LinkFox gateway to call 24 Temu Manage Product APIs for listing, detail, SKU, stock, editing, deletion, compliance, and sale-status workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to query and update Temu Global catalog items through LinkFox, including inventory, SKU data, compliance fields, publishing status, sale status, and deletion workflows.

### Deployment Geography for Use:

Global (Temu Global site; US and EU workflows are documented as separate skills)

## Known Risks and Mitigations:

Risk: The skill sends LinkFox and Temu credentials through the LinkFox gateway.

Mitigation: Install only if you trust LinkFox, use scoped credentials where possible, avoid pasting secrets into shared logs, and rotate or revoke tokens after sensitive work.

Risk: Temu access tokens and full API responses can be stored locally.

Mitigation: Use a controlled workspace, set the token-store path deliberately when needed, review saved linkfox data files, and remove sensitive local artifacts after the task is complete.

Risk: The skill includes product mutation and delete operations for inventory, compliance, sale status, and product records.

Mitigation: Review generated parameters before execution, prefer read-only query/detail commands first, and require explicit user confirmation before edit, delete, or status-change commands.

Risk: The generic proxy and billing-onboarding scripts broaden what the skill can do beyond narrow product lookups.

Mitigation: Avoid generic proxy or payment commands unless the user explicitly requests them, and clarify operation scope and possible charges before continuing.

## Reference(s):

- [API reference](artifact/references/api.md)
- [Partner Global catalog](artifact/references/partner-global-catalog.md)
- [Per-interface API documents](artifact/references/apis/README.md)
- [Temu access token guidance](artifact/references/access-token.md)
- [Onboarding and authentication guidance](artifact/references/onboarding.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2a343c65a03d42d380e9ad835aa7b54b)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses printed to stdout or saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses are printed in full; larger responses are summarized while full response JSON is saved under a local linkfox session directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
