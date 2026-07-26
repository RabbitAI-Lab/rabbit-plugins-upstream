## Description: <br>
Rewrites AI-generated serious nonfiction in English or Chinese to read human in academic or popsci mode while preserving source facts and abstaining when the draft already reads human. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External writers, researchers, editors, and developers use this skill to revise AI-looking thesis, abstract, literature review, research report, policy report, or serious popular-science prose while preserving register and facts. It can also run a detect-only diagnostic mode that returns a signal map instead of rewriting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes and may edit user-provided academic or serious nonfiction drafts. <br>
Mitigation: Use it only on drafts the user intends to share with the agent, and review the final text before relying on it. <br>
Risk: A rewrite could accidentally alter meaning or introduce unsupported detail. <br>
Mitigation: Preserve every source fact, citation, number, quotation, named entity, and date; compare added clauses against the source before accepting the result. <br>
Risk: The local detector is diagnostic and cannot reliably separate clean modern AI prose from clean human prose. <br>
Mitigation: Treat detector output as a signal map, not as a pass/fail decision; use editorial judgment and the blind-judge rubric for quality checks. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentjiang06/skills/humanizer-academic) <br>
- [Skill Behavior Specification](SKILL.md) <br>
- [Academic Pack](references/academic-pack.md) <br>
- [Popsci Pack](references/popsci-pack.md) <br>
- [English Patterns](references/lexical-en.md) <br>
- [Chinese Patterns](references/lexical-zh.md) <br>
- [Structural and Statistical Signals](references/structural-signals.md) <br>
- [Blind-Judge Rubric](references/blind-judge-rubric.md) <br>
- [Detect AI Signals Script](scripts/detect_ai_signals.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Plain text or Markdown for rewrites and notes; JSON for detect-only signal maps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May abstain and return unchanged source text; substantial rewrites may include a concise change note when requested.] <br>

## Skill Version(s): <br>
4.0.0 (source: SKILL.md frontmatter metadata.version, CHANGELOG.md, evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
