## Description: <br>
Call Bridge helps an agent plan and operate AI-assisted phone workflows, including parallel outbound calls, live handoff, inbound call preferences, campaign follow-up, voice settings, and error recovery guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teams and individuals can use this skill to prepare outbound call tasks, compare information across multiple calls, bridge a user into sensitive conversations, configure inbound handling rules, and manage follow-up state for telephony campaigns. <br>

### Deployment Geography for Use: <br>
Use where Call Bridge service access, U.S. +1 phone numbers, and local calling, recording, consent, privacy, and telemarketing requirements are satisfied. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place, bridge, forward, and retry real phone calls. <br>
Mitigation: Require explicit user confirmation before each outbound call, bridge, forwarding change, retry, or campaign action. <br>
Risk: API keys and sign-in links may expose control of the telephony service. <br>
Mitigation: Protect stored keys, restrict file permissions, avoid logging secrets, and rotate keys if disclosure is suspected. <br>
Risk: Transcripts and campaign state may contain sensitive personal, financial, or identity-verification details. <br>
Mitigation: Minimize stored transcript content, avoid retaining sensitive details, and review privacy and consent obligations before use. <br>
Risk: The package includes unrelated review and scoring documentation, creating confusion about the skill's behavior. <br>
Mitigation: Review the skill text before broad deployment and remove or correct unrelated documentation. <br>


## Reference(s): <br>
- [Call Bridge skill listing](https://clawhub.ai/thcjp/skills/call-bridge) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with cURL examples, JSON configuration snippets, call-state structures, and operational guidance.] <br>
**Output Parameters:** [Call targets, task instructions, bridge_number, voice, personality, greeting, inbound instructions, handoff_number, API key, campaign state, and transcript context.] <br>
**Other Properties Related to Output:** [The skill may guide agents to make or manage real calls, bridge users into live calls, configure forwarding behavior, poll call history, and handle stored API keys or transcript-derived campaign state.] <br>

## Skill Version(s): <br>
1.0.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
