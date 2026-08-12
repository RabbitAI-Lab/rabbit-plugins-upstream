## Description:

Screens recent A-share buyback announcements across the Shanghai, Shenzhen, and Beijing exchanges, filters by valuation and buyback criteria, and returns tabular results from Eastmoney Data Center.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lucky-dreamer](https://clawhub.ai/user/lucky-dreamer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to identify recent A-share company buyback announcements, apply PE, PB, market-cap, amount, purpose, progress, and date-window filters, and summarize or export the resulting company list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Eastmoney public market-data services.

Mitigation: Run it only where outbound access to Eastmoney endpoints is approved and expected.

Risk: The script writes a TSV result file in the current working directory.

Mitigation: Use the documented --out option or run it in a controlled working directory before sharing generated files.

Risk: Outputs are market-data screening results and may be mistaken for investment advice.

Mitigation: Treat outputs as screening inputs, verify announcements and market data independently, and avoid presenting results as financial advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lucky-dreamer/skills/buyback-screen)
- [Eastmoney Data Center API](https://datacenter-web.eastmoney.com/api/data/v1/get)
- [Eastmoney stock announcement API](https://np-anotice-stock.eastmoney.com/api/security/ann?sr=-1&page_size=50&page_index=1&ann_type=A&client_source=web&stock_list=000333)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown tables on stdout plus UTF-8 TSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access to Eastmoney public data APIs; default window is 14 days unless a date range is supplied.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
