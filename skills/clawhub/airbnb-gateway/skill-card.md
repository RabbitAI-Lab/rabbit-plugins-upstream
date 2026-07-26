## Description: <br>
Airbnb Gateway standardizes how agents operate Airbnb host workflows, including inbox and thread reads, reservation and calendar inspection, draft replies, verified message sending, and operator-approved calendar mutations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jason-vaughan](https://clawhub.ai/user/jason-vaughan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and vacation-rental operators use this skill to make OpenClaw-style agents handle Airbnb messaging, reservation lookup, calendar review, and approved calendar changes consistently. It is intended for accounts the operator controls, with human approval and verification for guest-facing or inventory-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect a live, revenue-bearing Airbnb account through guest messages and approved calendar mutations. <br>
Mitigation: Install only where the operator controls the Airbnb account, enforce the approval policy, and keep calendar mutations human-in-the-loop with fresh-load verification. <br>
Risk: A successful send acknowledgment can be mistaken for a guest-visible message. <br>
Mitigation: Treat send success as attempted until the live thread is re-read and the outbound message is visibly confirmed; do not auto-resend unconfirmed messages. <br>
Risk: A wrong role-to-tool mapping can send agents through unsafe or unavailable tool paths. <br>
Mitigation: Verify the deployment-specific role mapping in references/airbnb-tool-priority.md before use and escalate when required roles are missing. <br>
Risk: The ClawBridge token or logged-in browser identity grants sensitive account access. <br>
Mitigation: Treat the token and browser session as sensitive credentials and run the skill only in controlled environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jason-vaughan/skills/airbnb-gateway) <br>
- [Airbnb Tool Priority](references/airbnb-tool-priority.md) <br>
- [Airbnb Message Send State Machine](references/airbnb-message-state-machine.md) <br>
- [Airbnb Safety Rules](references/airbnb-safety-rules.md) <br>
- [Calendar Mutation Procedure](references/calendar-mutation-procedure.md) <br>
- [Future Adapter Interface](references/future-adapter-interface.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with command verbs, structured status reports, escalation reports, and inline shell commands where a deployment requires them.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are scoped by operation tier; sends and calendar mutations require approval and post-action verification, while unsafe or ambiguous states produce escalation guidance.] <br>

## Skill Version(s): <br>
0.2.1 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
