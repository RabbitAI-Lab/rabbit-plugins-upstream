## Description: <br>
KallyAI Executive Assistant helps agents use the KallyAI CLI and API for delegated calls, inbound call handling, email, bookings, research, errands, messaging, phone number management, outreach, credits, subscriptions, and referrals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sltelitsyn](https://clawhub.ai/user/sltelitsyn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to delegate real-world executive-assistant tasks through KallyAI, including calls, emails, bookings, searches, inbound call handling, messaging, budget checks, and account or subscription actions. <br>

### Deployment Geography for Use: <br>
Global, subject to KallyAI supported-country restrictions. <br>

## Known Risks and Mitigations: <br>
Risk: Broad natural-language delegation can initiate calls, emails, bookings, spending-related actions, outreach, subscriptions, phone routing, and account changes without clear approval boundaries. <br>
Mitigation: Review OAuth permissions, set explicit limits for each action category, and require manual confirmation before third-party contact, purchases, subscription changes, or account changes. <br>
Risk: The integration can expose sensitive operational data such as stored tokens, call recordings, transcripts, inbound rules, connected channels, and imported contacts. <br>
Mitigation: Periodically review active goals, inbound rules, connected channels, stored tokens, recordings, transcripts, and contact imports; remove stale access and data when it is no longer needed. <br>
Risk: Phone number provisioning, forwarding, caller ID, and inbound routing can affect real calls and caller experience. <br>
Mitigation: Confirm supported countries and phone-routing settings before enabling them, monitor inbound and outbound call history, and keep a manual takeover or rejection path available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sltelitsyn/skills/kallyai) <br>
- [KallyAI API base URL](https://api.kallyai.com) <br>
- [KallyAI OAuth authorization endpoint](https://api.kallyai.com/v1/auth/authorize) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the kallyai CLI and OAuth authentication; actions may create or retrieve calls, emails, bookings, messages, budgets, contacts, phone routing, and account-management results.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
