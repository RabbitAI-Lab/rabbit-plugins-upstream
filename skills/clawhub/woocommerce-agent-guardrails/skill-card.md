## Description: <br>
Safety guardrails for AI agents writing to a live WooCommerce store via MCP or the REST API, including approval gates, dry-run previews, bulk-change caps, failure circuit breakers, and prompt-injection defense for untrusted commerce data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arbazex](https://clawhub.ai/user/arbazex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and store operators use this skill to constrain AI agents that create, update, delete, or bulk-modify WooCommerce products, prices, inventory, orders, coupons, or customer data. It is intended for live-store automation where write actions need previews, explicit approval, and failure handling before production data is changed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents operating on a live WooCommerce store can make public or irreversible changes to products, prices, orders, coupons, customer data, or store settings. <br>
Mitigation: Use dry-run previews, before-and-after tables, explicit confirmations, staged batches, and stricter confirmation for deletes, storewide changes, large price changes, and exports. <br>
Risk: Repeated write failures can leave a store partially updated or hide structural problems such as invalid IDs, expired credentials, or schema mismatches. <br>
Mitigation: Stop after three consecutive write failures and report which items succeeded, failed, or remain untouched before continuing. <br>
Risk: Supplier feeds, scraped pages, product descriptions, reviews, or customer notes can contain prompt-injection text disguised as commerce data. <br>
Mitigation: Treat external content as data rather than instructions, flag rows that look like commands, and skip suspicious rows until the user confirms the intended handling. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/arbazex/woocommerce-agent-guardrails) <br>
- [ClawHub skill page](https://clawhub.ai/arbazex/skills/woocommerce-agent-guardrails) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/arbazex) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown guidance with tier definitions, approval gates, dry-run preview expectations, and confirmation language.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes hard caps, a repeated-failure circuit breaker, a kill switch, and prompt-injection handling guidance for imported or scraped commerce content.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
