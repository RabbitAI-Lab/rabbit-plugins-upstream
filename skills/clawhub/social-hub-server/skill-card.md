## Description: <br>
Social Hub Server is a centralized relationship-matching engine that coordinates user agents, stores profile signals, evaluates potential matches, and manages confirmation and feedback workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freeai-io](https://clawhub.ai/user/freeai-io) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to run a trusted central matching service for personal agents. It coordinates profile updates, match scoring, notifications, confirmations, scheduled scans, and feedback for a small multi-user relationship-matching network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill centralizes sensitive multi-user profile and relationship data. <br>
Mitigation: Operate it only in a trusted service context with defined membership, data retention, consent, review, and deletion processes. <br>
Risk: Profile data may be stored locally and sent to embedding or LLM providers during matching. <br>
Mitigation: Define and document which profile fields may be stored or sent to providers, and apply the user's disclosure settings before sharing match-facing information. <br>
Risk: Group logs can expose operational details or user relationship activity. <br>
Mitigation: Restrict log access, avoid unnecessary sensitive details in logs, and define who may read or export operational logs. <br>
Risk: Recurring automated scans and match notifications can act on stale or unauthenticated messages. <br>
Mitigation: Authenticate group messages, validate sender identity, and expire or refresh profile data before scheduled matching decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/freeai-io/skills/social-hub-server) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON message and storage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational log message formats, scheduled task guidance, and privacy-filtering rules.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
