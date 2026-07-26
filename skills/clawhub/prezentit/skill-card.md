## Description: <br>
Generate AI-powered presentations with custom themes, visual designs, speaker notes, and downloadable outputs through the Prezentit API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vegovevo](https://clawhub.ai/user/vegovevo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to check Prezentit credits, choose themes, generate presentation slide decks from a topic or outline, share the resulting view URL, and optionally download PPTX, PDF, or JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Presentation topics, outlines, details, and design prompts are sent to the Prezentit API. <br>
Mitigation: Avoid confidential or regulated content unless approved for this service. <br>
Risk: The skill requires a Prezentit API key and can spend credits when generating or retrying presentations. <br>
Mitigation: Use a Prezentit-specific API key, check available credits first, show the expected cost, and wait for user confirmation before generation or retry. <br>
Risk: Streaming generation responses can cause agent handling issues. <br>
Mitigation: Set `stream` to `false` for generation requests. <br>


## Reference(s): <br>
- [Prezentit skill page](https://clawhub.ai/vegovevo/skills/prezentit) <br>
- [Prezentit homepage](https://prezentit.net) <br>
- [Prezentit API key management](https://prezentit.net/api-keys) <br>
- [Prezentit buy credits](https://prezentit.net/buy-credits) <br>
- [Prezentit support](https://prezentit.net/support) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with HTTP examples and JSON request or response bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces presentation view URLs and optional PPTX, PDF, or JSON downloads through the Prezentit API.] <br>

## Skill Version(s): <br>
1.0.11 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
