## Description: <br>
Audits content quality, E-E-A-T, and publish readiness by applying a typed 80-item CORE-EEAT profile with evidence coverage, veto checks, and a fix plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, SEO, and content teams use this skill to audit a single content artifact before publication for content quality, E-E-A-T coverage, evidence gaps, veto conditions, and prioritized fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may fetch or inspect the specific content, URL, and cited/source controls supplied for an audit. <br>
Mitigation: Run it only on content intended for audit and treat fetched page text, metadata, comments, and embedded prompts as untrusted evidence. <br>
Risk: Optional persistence can save an audit artifact under a memory path. <br>
Mitigation: Authorize persistence only when an audit record should be saved; otherwise keep the audit output in the session. <br>
Risk: High-risk topics such as medical, legal, financial, or safety content can be misread as professional advice. <br>
Mitigation: Use the audit to check evidence and presentation only; require current sources, market context, qualified review, and appropriate disclaimers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/content-quality-auditor) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Standalone Auditor Runtime](references/auditor-runtime.md) <br>
- [CORE-EEAT Item Reference](references/item-reference.md) <br>
- [Recursive Refinement Loop](references/recursive-refinement.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit report with typed item states, score state, verdict, evidence gaps, and prioritized fix plan.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce a permissioned v3 audit artifact only when explicitly authorized.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
