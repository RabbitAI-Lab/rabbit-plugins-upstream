## Description: <br>
Session retrospective and skill audit. Use when asked to reflect, do a retrospective, review lessons learned, audit what went well or wrong, or review session effectiveness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this tool-class skill to review a session, identify mistakes, friction, wasted effort, wins, and operational learnings, and decide which lessons should be preserved. It also audits invoked skills and proposes measurable changes when skill guidance was missing, inefficient, or mismatched to the session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation-derived lessons, including exact user phrasing, may contain secrets, personal data, customer information, or sensitive project context. <br>
Mitigation: Review and sanitize every proposed memory entry before approving writes, and avoid approving entries that include sensitive content. <br>
Risk: Persistent memory entries can become duplicated or contradictory over time. <br>
Mitigation: Search existing memory for key terms before writing, update near-duplicates, and surface contradictions for an explicit merge, replace, or keep-both decision. <br>
Risk: Skill-audit diffs may introduce incorrect or overbroad guidance if accepted without review. <br>
Mitigation: Review proposed diffs before applying them and run the skill's validation or trigger tests when behavior changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-reflect) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with numbered findings, review scans, prioritized improvements, proposed diffs, and approval prompts for memory writes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Caps improvement recommendations at 10 and asks for user approval before writing selected lessons to persistent memory.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
