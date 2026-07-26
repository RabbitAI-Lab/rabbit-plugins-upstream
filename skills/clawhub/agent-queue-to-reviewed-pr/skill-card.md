## Description: <br>
Turn a ticket queue into reviewed draft PRs with an agent that never merges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to wire an agent to a prioritized ticket board or issue tracker so it can ground work, run checks, open draft PRs, and leave review and merge decisions to humans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queue and acknowledgment endpoints can move ticket, brief, PR, and run-status data across the network. <br>
Mitigation: Configure only the intended endpoints, use the dedicated agent bearer token, and keep the skill inert by leaving endpoint variables unset until deployment is deliberate. <br>
Risk: A broad forge token could allow actions beyond opening draft PRs. <br>
Mitigation: Provision a fine-grained token limited to one repository with contents:write and pull_requests:write, and verify merge and protected-branch writes fail before autonomous use. <br>
Risk: Browser QA screenshots may contain authenticated session data. <br>
Mitigation: Use a dedicated preview/test browser profile, avoid production tenants and personal profiles, and run the provided retention workflow so screenshots are deleted at PR close or within seven days. <br>
Risk: If the work source lacks conditional writes, failures can leave items stuck as claimed or in progress. <br>
Mitigation: Confirm claims by read-back, write terminal failure states explicitly, and reclaim stale claims by TTL when using non-transactional queues. <br>


## Reference(s): <br>
- [Agent Queue To Reviewed Pr on ClawHub](https://clawhub.ai/alexbloch-ia/skills/agent-queue-to-reviewed-pr) <br>
- [Publisher profile](https://clawhub.ai/@AlexBloch-IA) <br>
- [Queue/ack HTTP contract](references/queue-contract.md) <br>
- [Grounding brief](references/grounding-brief.md) <br>
- [Browser QA of the preview, and remediation](references/browser-qa.md) <br>
- [Brief staleness](references/brief-staleness.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell command examples and helper Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational instructions for queue polling, grounding, draft PR creation, browser QA, drift checks, and local retention.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
