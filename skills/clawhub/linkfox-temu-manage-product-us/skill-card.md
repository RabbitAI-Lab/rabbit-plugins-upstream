## Description:

This skill helps agents manage Temu US catalog products through LinkFox-forwarded Partner US Manage Product APIs for product lists, details, SKU queries, stock, status, compliance, updates, and deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and e-commerce operators use this skill to query and manage live Temu US product catalog data via LinkFox, including product edits, inventory changes, listing status, compliance fields, and deletion.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill can mutate live Temu US catalog data, including delete, full-update, stock, and status operations.

Mitigation: Review each requested mutation and its target product identifiers before execution, especially delete, full-update, stock, status, and compliance requests.

Risk: The skill handles LinkFox API keys and Temu access tokens, and may use local token storage.

Mitigation: Treat all LinkFox and Temu tokens as secrets, avoid plaintext production tokens, and use the minimum access needed for the task.

Risk: The generic proxy and file-download scripts can reach broader LinkFox or Temu operations than a single fixed endpoint.

Mitigation: Use operation-specific scripts when possible and inspect the requested API type, site, and parameters before running generic proxy or file-download commands.

Risk: The onboarding and billing flow may affect account access or payment state.

Mitigation: Confirm the account, quota, and payment intent with the user before following onboarding or recharge guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-manage-product-us)
- [Temu Partner US Manage Product documentation](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2a343c65a03d42d380e9ad835aa7b54b)
- [API reference](references/api.md)
- [Partner US API catalog](references/partner-us-catalog.md)
- [Per-interface API references](references/apis/README.md)
- [Access token guide](references/access-token.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may save full API responses as JSON files under the working directory and print either full JSON or summaries depending on response size.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
