## Description: <br>
Clawcall lets an agent place real U.S. phone calls, handle phone menus or wait time, bridge users into calls, and return call status, transcripts, results, and recording links when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use Clawcall to delegate U.S. phone calls for reservations, business inquiries, customer-service queues, order confirmations, option comparisons, and user-bridged calls that may need live decisions or identity checks. <br>

### Deployment Geography for Use: <br>
Global; outbound calling is limited to U.S. +1 phone numbers. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to make real phone calls, including calls that may involve commitments, cancellations, purchases, identity checks, or other sensitive decisions. <br>
Mitigation: Require clear user authorization and decision boundaries before calls, avoid parallel calls that could create duplicate commitments, and use user bridge or handoff for sensitive or irreversible steps. <br>
Risk: The skill stores and reuses a voice-call API key and user phone number locally. <br>
Mitigation: Store credentials and phone numbers only in approved local secret storage or restricted configuration files, review saved values before bridge or handoff calls, and remove stale or incorrect values promptly. <br>
Risk: Transcripts, recording links, sign-in URLs, and call results may contain sensitive account or personal information. <br>
Mitigation: Treat transcripts, recordings, and sign-in links as sensitive data, share only what is needed for the user outcome, and avoid highly sensitive calls unless the user confirms the risk. <br>
Risk: The artifact states that the skill is not suitable for emergency response, medical emergencies, or decisions requiring 100 percent determinism. <br>
Mitigation: Do not use the skill for emergency assistance or critical deterministic decisions; route those situations to appropriate human or emergency channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/clawcall) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [Voice Call API base URL](https://api.voicecall.example) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API payload examples, shell-style HTTP examples, call status summaries, transcripts, and recording links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist a voice-call API key and user phone number locally; supports U.S. +1 phone numbers and up to 3-4 parallel information-only calls.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
