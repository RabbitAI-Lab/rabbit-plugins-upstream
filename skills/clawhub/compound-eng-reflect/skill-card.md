## Description: <br>
Session retrospective and skill audit for reflecting on sessions, reviewing lessons learned, and auditing what went well or wrong. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to review a completed session, identify mistakes, friction, wasted effort, and wins, and decide which lessons should be preserved. It also audits invoked skills and proposes concrete improvements or diffs when skill changes are warranted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved memories or skill edits can influence future agent behavior if approved without review. <br>
Mitigation: Review each proposed memory entry or skill diff before approving persistence. <br>
Risk: Session retrospectives may quote or summarize sensitive conversation content. <br>
Mitigation: Do not persist secrets, credentials, private URLs, customer data, unredacted personal information, or machine-specific paths. <br>


## Reference(s): <br>
- [ia-reflect on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-reflect) <br>
- [Skill specification](artifact/SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with findings, prioritized improvements, review prompts, and proposed diffs when skill audits are requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose memory entries or skill edits for user approval; review proposed changes before they are persisted.] <br>

## Skill Version(s): <br>
4.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
