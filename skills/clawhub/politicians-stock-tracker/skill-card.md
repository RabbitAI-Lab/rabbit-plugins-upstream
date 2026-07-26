## Description: <br>
Tracks U.S. congressional stock trades from official House Clerk and Senate eFD disclosures through the read-only SentiSense Politicians Trading API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users and agents use this skill to look up recent congressional trades, per-ticker trading history, active politicians, and individual member profiles. It is intended for informational analysis of public disclosure data, not order entry, portfolio management, or personalized investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SentiSense API key for congressional trading lookups. <br>
Mitigation: Install only when the runtime can protect SENTISENSE_API_KEY, keep the key out of prompts and user-facing output, and use it only for read-only requests. <br>
Risk: Congressional trading data can be misread as investment advice or a trading signal. <br>
Mitigation: Treat results as informational, verify important financial conclusions independently, and do not use the skill by itself for trading decisions. <br>
Risk: STOCK Act filings report amount ranges and may be disclosed after the transaction date. <br>
Mitigation: Report amount bands rather than precise values and distinguish transaction dates from disclosure dates, including disclosure delay when available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker) <br>
- [SentiSense homepage](https://sentisense.ai) <br>
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key) <br>
- [SentiSense pricing](https://app.sentisense.ai/pricing?coupon=AGENTS26) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries with optional inline curl or Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only API lookups requiring SENTISENSE_API_KEY; results should preserve disclosure dates, transaction dates, amount ranges, and preview limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
