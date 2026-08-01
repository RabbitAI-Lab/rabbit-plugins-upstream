## Description: <br>
Provides a Python reference implementation of the Kimi K3 subagent architecture with two-stage batch scheduling, lifecycle management, event tracking, profile-based tool access, and rate-limit handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent engineers can use this skill as a subagent scheduling reference for spawning, resuming, retrying, batching, and tracking subagent work with built-in profiles and rate-limit backoff behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Profiles may allow shell, write, edit, web search, or web fetch capabilities when wired into an agent runtime. <br>
Mitigation: Run the skill in a scoped workspace, review prompts before launching background or batch work, and limit profile tool access to the intended task. <br>
Risk: The release evidence notes correctness gaps around resume and retry preserving real prior context. <br>
Mitigation: Do not rely on resume or retry continuity for critical workflows until that behavior is verified in the target runtime. <br>
Risk: Batch subagent execution can increase concurrency and provider rate-limit exposure. <br>
Mitigation: Use explicit concurrency limits and monitor rate-limit behavior before applying the batch scheduler to high-volume workloads. <br>


## Reference(s): <br>
- [Kimi K3 Subagent Architecture Notes](references/kimi-k3-subagent-architecture.md) <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/kimi-k3-subagent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python code examples and configuration-oriented details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces subagent scheduling patterns, profile definitions, and operational guidance for agent workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
