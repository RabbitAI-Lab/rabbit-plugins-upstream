## Description: <br>
Locates and explains AdsBrain/Codewiz Langfuse trace errors by querying XRay/Langfuse trace data and reporting the faulty observation, supporting evidence, responsibility, and fix suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lizejia668-code](https://clawhub.ai/user/lizejia668-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to diagnose AdsBrain/Codewiz agent behavior from Langfuse/XRay traces, identify the faulty observation or component, and produce concise root-cause evidence and fix suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trace analysis may expose prompts, payloads, session IDs, and business data from Langfuse/XRay. <br>
Mitigation: Install only in environments where this trace access is appropriate, and review generated reports so they include only the evidence needed for debugging. <br>
Risk: The workflow relies on a declared local xray-ai-trace-analysis helper path and dependency. <br>
Mitigation: Confirm the helper path and xray-ai-trace-analysis dependency are trusted and available before running trace queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lizejia668-code/skills/adsbrain-trace-error-locator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Concise Markdown root-cause report with trace/session links, evidence bullets, and fix suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default reports avoid full trace dumps and long prompts; detailed timelines are produced only when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
