## Description:

Helps Amazon sellers and operators analyze collected reviews to identify high-frequency terms, co-occurring words, buyer praise and complaints, and keyword ideas for Listings and ads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill through an agent to extract customer wording, review themes, keyword candidates, and concise analysis from ARI-collected Amazon review data. It can also guide related review workflows such as reports, exports, monitoring, competitor comparisons, and billing-aware confirmations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses an ARI API key locally for account access.

Mitigation: Install it only for ARI accounts you intend to connect, do not paste API keys into chat, and remove or rotate the key if the local environment is no longer trusted.

Risk: Some collection and analysis workflows can spend credits, including account-level auto-confirmed actions.

Mitigation: Set autoconfirm off when every paid action should be approved first, and require clear confirmation before running workflows that may charge credits.

Risk: The package includes capabilities beyond keyword extraction, including monitoring, competitor, export, and workbench workflows.

Mitigation: Confirm those adjacent actions explicitly and review returned costs, plan limits, and account changes before enabling them.

Risk: Changing ARI_BASE_URL could redirect authenticated CLI requests away from the official ARI service.

Mitigation: Avoid custom ARI_BASE_URL settings unless you control the endpoint and have intentionally enabled the companion custom-base safeguard.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-keywords)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Conversational text or Markdown, with optional CLI-produced JSON, CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some review collection, analysis, monitoring, export, and account actions may depend on credits, plan limits, and explicit or account-level confirmation settings.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, _meta.json, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
