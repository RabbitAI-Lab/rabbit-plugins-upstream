## Description: <br>
This skill helps PRC government-procurement purchasers and procurement agents match similar complaint decisions, compare sustained and rejected objection patterns, identify reply risks, and draft compliant supplier-objection responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement staff, procurement agents, and legal reviewers use this skill after receiving a supplier objection in a PRC government-procurement project to find similar administrative decisions, assess whether the proposed response is weak, and prepare a review-ready reply letter draft. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may encourage persistent edits to installed skill or reference files after use. <br>
Mitigation: Require explicit user approval before any write to SKILL.md or reference files, or disable those write-back instructions in deployed environments. <br>
Risk: Generated procurement-law conclusions, case matches, and deadlines may be incomplete or wrong if source retrieval is unavailable or outdated. <br>
Mitigation: Treat outputs as drafts and require qualified procurement or legal staff to verify cited laws, source decisions, evidence, and response deadlines before use. <br>
Risk: The skill is scoped to mainland China government-procurement objections and can mislead users if applied to engineering bidding disputes or Hong Kong, Macau, or Taiwan legal contexts. <br>
Mitigation: Route out-of-scope matters to the appropriate workflow and require the output to exclude non-mainland legal materials when making PRC government-procurement recommendations. <br>


## Reference(s): <br>
- [README](artifact/README.md) <br>
- [Case Matching Guide](artifact/references/case-matching-guide.md) <br>
- [Reply Letter Template](artifact/references/reply-letter-template.md) <br>
- [Risk Pattern Library](artifact/references/risk-pattern-library.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured tables and draft legal-response text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite knowledge-base sources for case and legal conclusions, mark unsupported claims as basis pending verification, and separate external reply drafts from internal risk predictions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, manifest.yaml, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
