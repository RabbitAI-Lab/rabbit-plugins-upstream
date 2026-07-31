## Description: <br>
Run an autonomous email inbox with Drin to receive inbound email on a domain, read conversation threads, and reply in-thread. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atom00blue](https://clawhub.ai/user/atom00blue) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure and operate a Drin-backed email inbox for agents that receive inbound messages, inspect conversation threads, and send approved replies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can expose email contents and send replies from a configured domain. <br>
Mitigation: Install only for agents intended to manage a real inbox, and configure Drin credentials, receiving domains, webhooks, and reply behavior carefully. <br>
Risk: Inbound mail or webhook events may be unauthenticated or processed more than once. <br>
Mitigation: Verify webhook signatures before trusting inbound events, honor suppressions, and track handled message IDs or idempotency keys before replying. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers Drin domain receiving, inbox creation, thread reading, webhook handling, in-thread replies, inbound simulation, and a minimal agent-loop pseudocode.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
