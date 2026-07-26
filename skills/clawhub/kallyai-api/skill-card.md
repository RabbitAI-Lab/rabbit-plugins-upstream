## Description: <br>
KallyAI Executive Assistant helps an agent use the KallyAI CLI to handle phone calls, inbound receptionist workflows, email, bookings, research, errands, multi-channel messaging, subscriptions, credits, and phone number management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sltelitsyn](https://clawhub.ai/user/sltelitsyn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to delegate KallyAI tasks from Claude Code, including calls, messages, bookings, searches, email, budget checks, subscriptions, and phone-number operations. It is intended for workflows where a human can review delegated actions before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad delegated authority over calls, email, bookings, orders, subscriptions, phone routing, connected channels, and other spending-related tasks. <br>
Mitigation: Require explicit user confirmation for recipients, message contents, calls, orders, bookings, cancellations, subscription changes, and phone-number or forwarding changes before execution. <br>
Risk: Authentication tokens enable access to KallyAI workflows on the local machine. <br>
Mitigation: Use the skill only on trusted machines, review KallyAI privacy and retention terms, and log out or revoke access when finished. <br>


## Reference(s): <br>
- [KallyAI API Reference](references/api-reference.md) <br>
- [KallyAI API](https://api.kallyai.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [JSON by default, with optional human-readable terminal tables and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses authenticated KallyAI API calls and can print structured error JSON.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
