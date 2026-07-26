## Description: <br>
Designs B2B cold-outbound email programs with sequence timing, reply-triage branches, warmup and sending throttles, compliance guardrails, and SEND S-dimension deliverability guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and revenue teams use this skill to plan B2B cold-outbound email sequences before drafting copy or sending campaigns. It helps map touch timing, reply routing, warmup and sending limits, jurisdiction guardrails, and deliverability handoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process business prospecting data and save summarized sequence decisions to memory after confirmation. <br>
Mitigation: Use appropriate data-handling controls for prospecting data and confirm before saving reusable summaries. <br>
Risk: Outbound email compliance depends on target jurisdictions, consent basis, opt-out handling, and internal policy. <br>
Mitigation: Verify jurisdiction-specific requirements and lawful-basis records with counsel or internal policy before sending. <br>
Risk: The generated sequence, warmup, and deliverability guidance is planning support rather than a send-ready legal or operational approval. <br>
Mitigation: Review the sequence, sender authentication, suppression handling, and platform configuration before campaign execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/cold-outbound-sequencer) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with sequence maps, branch tables, ramp schedules, guardrail blocks, and handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose saving summarized sequence decisions to memory after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: release evidence, SKILL.md frontmatter, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
