## Description: <br>
Perform paid OSINT lookups on usernames or emails to find public profiles and footprint data, paid in USDC on Base via x402 with no API keys needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jienweng](https://clawhub.ai/user/jienweng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run paid, public-profile OSINT lookups for legitimate recruiting research, prospecting, due diligence, trust and safety, brand protection, or a person's own exposure audit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet-based paid API calls can expose funds or incur unintended charges. <br>
Mitigation: Use a dedicated low-balance Base wallet, set MAX_SPEND_PER_CALL, and review the prompt and cost before approving payment. <br>
Risk: Submitted usernames, emails, prompts, media URLs, and agent identity details may be visible to the external service. <br>
Mitigation: Avoid submitting sensitive identifiers unless there is a legitimate basis, and assume submitted data may be processed by the service. <br>
Risk: OSINT results can be misused for harassment, stalking, or unlawful profiling. <br>
Mitigation: Limit use to public-profile research for legitimate purposes such as due diligence, trust and safety, brand protection, or a person's own exposure audit. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jienweng/skills/x402-osint) <br>
- [Free trial username lookup endpoint](https://x402-osint.tail66f665.ts.net/trial/osint/{username}) <br>
- [Paid username lookup endpoint](https://x402-osint.tail66f665.ts.net/osint/{username}) <br>
- [Paid identity report endpoint](https://x402-osint.tail66f665.ts.net/report/{username}) <br>
- [Paid email lookup endpoint](https://x402-osint.tail66f665.ts.net/email/{address}) <br>
- [MCP server endpoint](https://x402-osint.tail66f665.ts.net:10000/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Configuration, Shell commands, Guidance] <br>
**Output Format:** [Markdown with endpoint examples, environment variables, and natural-language lookup summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid endpoints return a natural-language summary field for agent use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
