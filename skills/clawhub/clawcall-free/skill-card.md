## Description: <br>
Clawcall Free lets an agent place basic outbound calls to real U.S. phone numbers, poll call status to finalization, and return call outcome details and a transcript. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent builders, and automation users use this skill to automate simple U.S. outbound phone calls, such as business inquiries or order-status checks, and receive structured call results. It is not suitable for emergency, medical, or other decisions requiring certainty. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real outbound phone calls. <br>
Mitigation: Use only when the user explicitly intends to place a call, verify the destination number, and avoid emergency or high-stakes use cases. <br>
Risk: Call instructions and transcripts can contain sensitive personal or business information. <br>
Mitigation: Keep task instructions limited to details needed for the call and review transcripts before sharing or storing them. <br>
Risk: API keys may be returned by the service and persisted locally. <br>
Mitigation: Treat API keys as secrets, prefer a secure key store, and avoid committing local credential files to version control. <br>
Risk: The release requests broader local authority than the calling workflow appears to require. <br>
Mitigation: Install with the minimum tool permissions needed, and restrict or remove exec access unless a documented workflow requires it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/clawcall-free) <br>
- [Voicecall API base URL](https://api.voicecall.example) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns call_id, API key when issued, lifecycle status, outcome, talk_seconds, and transcript; may persist API credentials locally.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter states 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
