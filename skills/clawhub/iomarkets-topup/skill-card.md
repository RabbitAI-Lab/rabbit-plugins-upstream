## Description:

IoMarkets Topup helps agents buy travel eSIMs and mobile airtime or data top-ups with USDC on Algorand via x402, with signed proof of delivery, automatic refunds, live catalog checks, and required human confirmation before purchase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sergovashakmadze](https://clawhub.ai/user/sergovashakmadze)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find, quote, buy, and verify travel eSIMs or mobile airtime and data top-ups for real phone service needs. It is useful when a human is traveling, needs mobile data abroad, wants to recharge a phone, or needs to check a USDC-to-local-currency rate before purchase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help spend USDC on real eSIMs or phone top-ups.

Mitigation: Confirm the delivered item, recipient phone number when applicable, operator, and USDC price with the human before approving a purchase.

Risk: A local MCP setup may hold a wallet mnemonic for automated payment signing.

Mitigation: Prefer hosted mode when wallet signing should stay outside the MCP server; when using local mode, keep the mnemonic in a protected file and set conservative per-session and per-order budgets.

Risk: Top-ups can be irreversible after delivery, and a wrong operator or phone number may produce an unusable purchase.

Mitigation: Read the phone number back verbatim, verify the operator with the human, and use lookup data carefully before buying.

## Reference(s):

- [IoMarkets Homepage](https://iomarkets.app)
- [IoMarkets Agent Documentation](https://iomarkets.app/agent.md)
- [ClawHub Skill Page](https://clawhub.ai/sergovashakmadze/skills/iomarkets-topup)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with HTTP request examples and MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces purchase workflow guidance, quote and order status handling instructions, receipt verification guidance, and MCP setup examples.]

## Skill Version(s):

0.2.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
