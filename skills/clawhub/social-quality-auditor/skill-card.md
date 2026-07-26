## Description: <br>
Audits social post batches or channel programs with ECHO checks for channel truth, claims, disclosure, manipulation, UGC rights, and measurement denominators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, social, and governance teams use it to decide whether a social asset batch is safe to publish or to baseline a channel program's operating maturity. It reports evidence-backed ECHO findings, unknowns, and fixes without posting or changing canonical records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit results could be mistaken for permission to publish or resume a social queue. <br>
Mitigation: Require separate explicit approval for publishing or queue changes; the skill itself should not post, unpause queues, or mutate registries. <br>
Risk: Missing private exports, permissions, claim records, or denominator evidence can make a score or verdict unreliable. <br>
Mitigation: List missing qualified items as unknown and avoid final scoring or gate decisions when required evidence is unavailable. <br>
Risk: Persisting an audit artifact without approval could create an unintended governance record. <br>
Mitigation: Write a v3 audit artifact only after explicit authorization and validate the artifact before persistence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/social-quality-auditor) <br>
- [Publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Standalone auditor runtime](references/auditor-runtime.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit report with typed status, verdict, score state, findings, unknowns, and fix guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a permissioned v3 audit artifact only after explicit authorization; otherwise produces inline audit guidance.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
