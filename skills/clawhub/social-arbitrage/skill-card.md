## Description: <br>
Researches current social, consumer, technology, cultural, weather, supply, and perception shifts and maps them to U.S.-listed equities using an evidence-gated social-arbitrage process. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiahongc](https://clawhub.ai/user/jiahongc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External finance researchers and agents use this skill to run current, evidence-gated social-arbitrage scans, map observable changes to eligible U.S.-listed equities, and produce research watchlists or report-ready triage. It is intended for public-information research and monitoring, not trade execution or personalized investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research-bias outputs could be mistaken for investment advice or trade instructions. <br>
Mitigation: Treat outputs as research triage only; do not use the skill for entries, exits, sizing, leverage, options, allocation, brokerage access, or trade execution. <br>
Risk: Social, search, market, and platform evidence can be stale, inaccessible, manipulated, sponsored, or derived from one source cluster. <br>
Mitigation: Record access gaps, require dated current evidence, establish a baseline, test authenticity, and require independent corroboration before elevating a candidate. <br>
Risk: Trend-to-ticker mappings can overstate issuer exposure, materiality, or the remaining information gap. <br>
Mitigation: Verify legal issuer identity, listing, security type, direct or verified second-order exposure, segment materiality, and market awareness from primary or authoritative sources before A/B classification. <br>
Risk: Possible material nonpublic information, private data, promotion, or account-gated platform context could contaminate the research process. <br>
Mitigation: Refuse to use possible MNPI, avoid exposing private personal information, reject manipulative promotion workflows, and rely only on public or user-authorized sources with disclosed access limits. <br>


## Reference(s): <br>
- [Skill release page](https://clawhub.ai/jiahongc/skills/social-arbitrage) <br>
- [Social Arbitrage Methodology](references/methodology.md) <br>
- [Research and Tool Playbook](references/research-playbook.md) <br>
- [Social Arbitrage Report Contract](references/report-template.md) <br>
- [Tearsheet interview with Chris Camillo](https://tearsheet.co/podcasts/how-to-beat-wall-street-by-using-facebook-reading-tabloids-and-shopping-with-chris-camillo/) <br>
- [Laughing at Wall Street excerpt](https://supadu.macmillan.com/folio-assets/book-excerpts/9780312657857EX.pdf) <br>
- [Investor.gov social-media stock scams](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/social-media-stock-scams) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown research reports, ranked watchlists, access ledgers, monitoring plans, and concise research-bias summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include as-of timestamps, dated source links, gate verdicts, falsifiers, counterarguments, data gaps, and clear boundaries against trade execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
