## Description: <br>
Queries the ClawEC API for Ozon hot product rankings with sales, GMV, price, fulfillment, cross-border eligibility, and related business filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cross-border ecommerce operators, product researchers, and agents use this skill to retrieve and interpret Ozon hot-selling product lists, competitor sales signals, and SKU selection opportunities from ClawEC data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ClawEC API key to access a third-party network service. <br>
Mitigation: Store the key in CLAWEC_API_KEY, avoid pasting secrets into chat, and review request filters before running API commands. <br>
Risk: Returned product rankings and business metrics come from a third-party API and may be incomplete, stale, or unsuitable for a specific purchasing decision. <br>
Mitigation: Treat the report as research input, verify important SKUs and marketplace conditions independently, and compare results across periods or filters before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-ozon-product-hot-ranking) <br>
- [Response schema](references/response-schema.md) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Chinese Markdown reports with product tables, curl or shell command examples, and JSON response interpretation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY for live API calls; pageSize is limited to 15 by the documented endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
