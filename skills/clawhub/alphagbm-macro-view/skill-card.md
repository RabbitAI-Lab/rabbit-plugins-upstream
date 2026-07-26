## Description: <br>
Tracks macro indicators such as VIX, Treasury yields, DXY, gold, oil, and BTC, then returns current readings and portfolio-linked impact analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to add, remove, list, and explain macro indicators through the AlphaGBM API. It is intended for portfolio-aware macro dashboards and concise impact summaries tied to a user's holdings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve portfolio-linked financial analysis from an external AlphaGBM API. <br>
Mitigation: Install only when the user is comfortable providing an AlphaGBM API key and sending portfolio-linked requests to the service. <br>
Risk: Broad macro or yield-related triggers may run the skill when the user's intent is ambiguous. <br>
Mitigation: Use clear, explicit requests for tracking, listing, or removing indicators, and confirm ambiguous macro requests before calling the API. <br>
Risk: Macro readings can become stale. <br>
Mitigation: Check last_updated_at in API responses and note when data is more than one day old. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/clementgu/skills/alphagbm-macro-view) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with HTTP examples, JSON response shapes, and table-first summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ALPHAGBM_API_KEY and may use ALPHAGBM_BASE_URL to override the default API host.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
