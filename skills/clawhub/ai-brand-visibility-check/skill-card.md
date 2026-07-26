## Description: <br>
Checks whether major AI assistants recommend a brand, product, or company for relevant best-in-category prompts, supporting GEO audits and competitive marketing research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rccola990-cloud](https://clawhub.ai/user/rccola990-cloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, GEO practitioners, and competitive research analysts use this skill to check whether AI assistants surface a brand and how competitor context appears in those answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill points agents to an external pay-per-call endpoint that may charge USDC through x402. <br>
Mitigation: Review the 402 price response before payment and only call the endpoint for an explicit user-requested brand visibility check. <br>
Risk: AI visibility results can be incomplete or time-sensitive and may be unsuitable as the sole basis for marketing claims. <br>
Mitigation: Treat results as research input, corroborate important claims with additional evidence, and disclose timing and query context in downstream reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rccola990-cloud/skills/ai-brand-visibility-check) <br>
- [Brand visibility check endpoint](https://store.agentexchange.work/brands/check) <br>
- [Sample catalog endpoint](https://store.agentexchange.work/samples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with a GET request example and concise brand visibility interpretation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an external pay-per-call x402 endpoint; the price is shown in the 402 response before payment.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
