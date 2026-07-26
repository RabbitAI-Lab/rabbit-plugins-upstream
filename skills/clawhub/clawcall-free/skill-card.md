## Description: <br>
Clawcall Free helps an AI agent place basic outbound calls to United States phone numbers, poll the call lifecycle to completion, and return the call outcome and transcript. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to make low-risk outbound calls for tasks such as merchant inquiries, information lookups, or order-status checks, then report the transcript-backed result. <br>

### Deployment Geography for Use: <br>
United States phone calls only <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill may place real outbound phone calls and send call instructions to an external service. <br>
Mitigation: Use it only for appropriate low-risk calls, confirm the target phone number and call objective before execution, and avoid emergency, medical, legal, or other high-stakes decisions. <br>
Risk: The skill may store an API key and phone number in ~/.config/voicecall/key.json. <br>
Mitigation: Manage file permissions for the local key file and delete it when credential retention is not desired. <br>
Risk: Returned transcripts may contain sensitive details from the call. <br>
Mitigation: Review transcripts before sharing them and avoid including private or unnecessary sensitive information in call instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/clawcall-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include call IDs, lifecycle status, outcome, talk duration, transcripts, and local API key configuration guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
