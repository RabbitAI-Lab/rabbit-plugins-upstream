## Description: <br>
Concord negotiates, redacts, and scores risks of sensitive data shared between agents, helping support privacy-aware transfers without requiring an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrea-cola](https://clawhub.ai/user/andrea-cola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Concord to negotiate and redact sensitive text before it is forwarded between agents or to external services. It can also support audit retrieval and token rehydration workflows when policy allows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive user text may be sent to an external Concord service before it is forwarded elsewhere. <br>
Mitigation: Use the skill with explicit user consent and avoid sending secrets unless policy allows it. <br>
Risk: The remote service's retention and rehydration behavior is unresolved in the provided evidence. <br>
Mitigation: Treat retention and token rehydration as review items until the publisher documents them clearly. <br>


## Reference(s): <br>
- [Concord ClawHub skill page](https://clawhub.ai/andrea-cola/skills/concord) <br>
- [Server-resolved GitHub provenance](https://github.com/andrea-cola/agent-to-agent-privacy/tree/dev/concord) <br>
- [Concord API service](https://concord-xybl.onrender.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, API calls, guidance] <br>
**Output Format:** [Markdown guidance with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return redacted outbound payloads, verdicts, risk scores, re-identification checks, attestations, and rehydrated text from a remote service.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
