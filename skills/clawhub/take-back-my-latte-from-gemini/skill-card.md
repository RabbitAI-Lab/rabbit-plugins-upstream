## Description: <br>
Analyze Gemini Cloud Billing and usage JSON, show actual Google AI spend in lattes, and estimate how many lattes the user could recover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and Gemini API users use this skill to analyze local Gemini Cloud Billing and usage JSON exports, summarize actual Gemini spend, and estimate directional recovery opportunities in a short latte-themed report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local Gemini billing or usage JSON selected by the user. <br>
Mitigation: Use only files you are comfortable analyzing locally, and avoid sharing raw billing details with the optional companion website unless separately reviewed. <br>
Risk: Recovery estimates may be mistaken for guaranteed savings. <br>
Mitigation: Treat estimated recoverable cost as directional and validate optimization changes with a small production test. <br>
Risk: Unsupported or unrelated billing data can lead to incomplete or rejected analysis. <br>
Mitigation: Use supported Google Cloud Billing JSON exports and Gemini or Vertex AI usageMetadata logs; do not rely on screenshots, invoices, CSV files, subscriptions, or non-Google provider data. <br>


## Reference(s): <br>
- [Supported input formats](references/input-formats.md) <br>
- [ClawHub skill page](https://clawhub.ai/margaretzybgl/skills/take-back-my-latte-from-gemini) <br>
- [Take Back My Latte companion site](https://take-back-my-latte.margaret-zybgl.chatgpt.site) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report grounded in local JSON analysis output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report is intended to stay under 250 words unless the user asks for detail; recovery estimates are directional.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
