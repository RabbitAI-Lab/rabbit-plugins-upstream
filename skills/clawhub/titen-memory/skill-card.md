## Description: <br>
Use a configured Titen MCP server to recall bounded evidence-grounded context, record verified durable signals, submit feedback, and coordinate checkpoints, leases, or handoffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ramaaditya49](https://clawhub.ai/user/ramaaditya49) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent should retrieve relevant project memory, preserve verified durable signals, or coordinate bounded checkpoints and handoffs through an authorized Titen memory service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recalled memory can be stale, untrusted, or inconsistent with the current repository or runtime. <br>
Mitigation: Verify recalled operational facts against current source or runtime before acting, and preserve conflicts or uncertainty. <br>
Risk: Memory writes could expose secrets, private raw conversations, chain of thought, or other inappropriate content. <br>
Mitigation: Store only verified durable signals, use the narrowest visibility and truthful trust level, and avoid secrets, raw transcripts, prompts, embeddings, and routine command output. <br>
Risk: A failed memory write could be mistaken for durable shared state. <br>
Mitigation: Report a memory item as durable only after the corresponding write succeeds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ramaaditya49/skills/titen-memory) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, text] <br>
**Output Format:** [Markdown or plain text guidance with MCP tool calls when the configured Titen tools are available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bounded recall and requires authorized subject and optional project scope for memory operations.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
