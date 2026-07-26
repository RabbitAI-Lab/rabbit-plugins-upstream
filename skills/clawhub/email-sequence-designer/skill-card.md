## Description: <br>
Designs email lifecycle automation flows with triggers, step timing, branch and exit conditions, cadence governance, sunset paths, and a SEND N-dimension score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, lifecycle, and growth teams use this skill to design welcome, cart-abandon, browse-abandon, post-purchase, light re-engagement, cold-outbound, cadence, and sunset flows before creative writing or final deliverability review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide scheduling live marketing broadcasts through Resend. <br>
Mitigation: Require explicit human approval before any live send and confirm the segment, subject, HTML, sender, and schedule. <br>
Risk: Marketing messages could be aimed at suppressed, non-consented, or incorrect recipients. <br>
Mitigation: Verify consent and suppression lists before enrollment and keep consent checks separate from sequence planning. <br>
Risk: Cadence, segmentation, or flow recommendations may be incorrect or misleading. <br>
Mitigation: Review flow maps, send caps, quiet hours, fatigue rules, and sunset thresholds before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/email-sequence-designer) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with lifecycle flow maps, cadence policy, handoff summary, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a reusable markdown handoff under memory/email/email-sequence-designer when the user confirms saving.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
