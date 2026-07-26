## Description: <br>
Agent Fact Check Verify helps agents assess factual claims with multiple public sources and return a concise Traditional Chinese fact-check conclusion with supporting links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nhzallen](https://clawhub.ai/user/nhzallen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to verify claims, especially Traditional Chinese requests asking whether information is correct. It guides the agent to consult public sources and return a four-part answer with a short verdict, the real situation, a conclusion, and up to five relevant links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Claim-related searches may be sent to Tavily or fallback search providers, and may query Reddit or Twitter/X tools when available. <br>
Mitigation: Avoid submitting private or sensitive claims unless those provider flows are acceptable for the deployment environment. <br>
Risk: Reliability may be reduced if referenced scripts or reference files are not supplied elsewhere. <br>
Mitigation: Verify the expected runtime tools and reference materials are available before relying on the workflow. <br>
Risk: Fact-checking output can be incomplete or outdated when public information is limited, unavailable, or behind paywalls. <br>
Mitigation: Review the supporting links and apply additional human review for medical, financial, legal, public-safety, or other high-impact claims. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/NHZallen/agent-fact-check-verify) <br>
- [ClawHub skill page](https://clawhub.ai/nhzallen/skills/agent-fact-check-verify) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Traditional Chinese Markdown with four fixed sections and up to five supporting links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Internal scoring is not shown to users; claim analysis is consolidated into a final answer.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
