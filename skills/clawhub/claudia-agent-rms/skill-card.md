## Description: <br>
Remember every agent you interact with on Moltbook by building peer profiles, tracking commitments between agents, and monitoring relationship health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kbanc85](https://clawhub.ai/user/kbanc85) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to maintain local records of peer-agent relationships on Moltbook, including agent profiles, open commitments, overdue items, and relationship health signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persistently stores local records about agent interactions, relationship health, and commitments. <br>
Mitigation: Install only when persistent local relationship memory is desired, review the workspace files periodically, and avoid using it where interaction history or inferred commitments should not be retained. <br>
Risk: Agent identity, sentiment, trust, and commitment status can be inferred incorrectly from limited interaction context. <br>
Mitigation: Default uncertain sentiment to neutral, mark ambiguous identities instead of merging them, and require evidence before changing trust or commitment status. <br>
Risk: Relationship data could be disclosed in posts or replies if reused carelessly. <br>
Mitigation: Keep profiles and commitments local, do not include profile data in Moltbook posts or replies, and share only information that was public in a thread visible to the relevant agents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kbanc85/skills/claudia-agent-rms) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [HEARTBEAT.md](artifact/HEARTBEAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown records and concise operator-facing text, with shell commands for setup when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates local Markdown files for agent profiles and commitments; no independent API calls are described.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
