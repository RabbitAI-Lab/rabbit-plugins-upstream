## Description: <br>
Coach helps an agent run goal-oriented coaching conversations, accountability check-ins, professional coaching workflows, and scope boundaries between coaching and adjacent forms of support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and coaches use this skill to structure coaching sessions, set and repair commitments, handle client intake and accountability, and decide when coaching should stop or refer to another form of support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can maintain durable local records about goals, commitments, clients, sponsors, rates, and sometimes health or finance metadata. <br>
Mitigation: Keep the Clawic data folder protected, avoid storing clinical disclosures or secrets, and review or delete records that should not remain in long-term coaching memory. <br>
Risk: Coaching output may be inappropriate for clinical care, crisis situations, or sensitive disclosures. <br>
Mitigation: Use the skill's referral and red-flag boundaries; stop coaching clinical or crisis issues and route the user to qualified professional or emergency support. <br>


## Reference(s): <br>
- [Coach on ClawHub](https://clawhub.ai/ivangdavila/skills/coach) <br>
- [Coach homepage](https://clawic.com/skills/coach) <br>
- [Session workflow](artifact/session.md) <br>
- [Accountability workflow](artifact/accountability.md) <br>
- [Memory template](artifact/memory-template.md) <br>
- [Referral and scope boundaries](artifact/referral.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Conversational text and Markdown notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local Clawic coaching records when configured, including goals, commitments, client notes, and follow-up dates.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
