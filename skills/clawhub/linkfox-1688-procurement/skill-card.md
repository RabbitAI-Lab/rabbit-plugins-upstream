## Description: <br>
Helps LinkFox users run authorized 1688 procurement workflows, including OAuth checks, SKU and address lookup, order preview, guarded order creation, payment URL retrieval, order tracking, logistics, cancellation, and receipt confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External LinkFox users and procurement operators use this skill to manage authorized 1688 sourcing fulfillment steps through LinkFox, from authorization and order preview through payment, logistics, cancellation, and receipt confirmation. It is intended for accounts that are allowed to operate the relevant 1688 procurement workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact procurement actions such as creating orders, retrieving payment URLs, cancelling orders, and confirming receipt. <br>
Mitigation: Require a separate Chinese natural-language confirmation immediately before each high-risk action, and rely on the script-level boolean confirmation gates before network calls. <br>
Risk: The skill depends on a LinkFox API key and optional gateway environment variable that authorize account-scoped procurement operations. <br>
Mitigation: Keep LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY and LINKFOX_TOOL_GATEWAY under user control, and do not expose API keys, tokens, callback codes, app secrets, session keys, or Authorization headers. <br>
Risk: Procurement responses may contain order, address, logistics, or other sensitive business data and may be saved when responses are large or saving is requested. <br>
Mitigation: Avoid saving responses unless needed, use no-save controls for sensitive sessions, and review saved redacted JSON before sharing or retaining it. <br>
Risk: Gateway calls may consume LinkFox credits and repeated retries or polling can increase cost or duplicate operational impact. <br>
Mitigation: Do not automatically retry failed, empty, unauthorized, or high-risk write operations; explain cost before additional calls and ask before continuing. <br>
Risk: Feedback about mismatches or user reactions may be reported to LinkFox. <br>
Mitigation: Be aware of the feedback-reporting behavior and avoid including unnecessary sensitive procurement details in feedback content. <br>


## Reference(s): <br>
- [1688 Procurement Workflow Map](artifact/references/workflow.md) <br>
- [1688 Procurement API Reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and redacted JSON responses or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Small responses are printed inline; larger redacted responses may be saved under a LinkFox workspace data directory unless saving is disabled.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
