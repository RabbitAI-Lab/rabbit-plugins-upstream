## Description: <br>
Monitors the Kannaka constellation across apps, services, swarm health, and NATS connectivity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickflach](https://clawhub.ai/user/nickflach) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to check constellation health, inspect connected swarm agents, monitor NATS transport, and diagnose cross-service issues across Kannaka components. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Joining a non-local NATS swarm bus can expose agent identifiers and live phase state to infrastructure outside the user's control. <br>
Mitigation: Confirm the NATS server before joining a swarm, prefer a local or controlled bus, and review KANNAKA_NATS_URL and swarm configuration. <br>
Risk: Status and listen commands can reveal live service availability, connected agents, and phase synchronization state. <br>
Mitigation: Run commands only against the intended constellation environment and avoid sharing outputs that disclose agent IDs or operational service state. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nickflach/skills/skill-kannaka-constellation) <br>
- [Kannaka radio reference deployment](https://radio.ninja-portal.com) <br>
- [Kannaka observatory reference deployment](https://observatory.ninja-portal.com) <br>
- [GhostSignals markets API](https://radio.ninja-portal.com/api/markets) <br>
- [Kannaka installer](https://radio.ninja-portal.com/download) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include service status, agent connectivity, NATS configuration, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.2.2 (source: ClawHub release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
