## Description: <br>
Pre-publication compliance and quality reviewer that checks factual citations, customer redaction, product naming, competitor rules, internal information, formatting, and AI traces, then outputs a pre-review report and fix suggestions without modifying the original. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content marketing and publication teams use this skill to review finished technology product drafts before release. It checks compliance-sensitive issues such as factual traceability, product naming, customer redaction, competitor references, internal information, formatting, and AI-like language, then reports issues and suggested fixes without changing the original draft. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger phrases such as "review" may activate the skill for work outside publication compliance review. <br>
Mitigation: Invoke it deliberately for pre-publication compliance review with a draft path and compliance profile, and prefer specific activation phrases for publication review. <br>
Risk: Review quality depends on current brand rules, sensitive-term lists, product-public-status data, customer-redaction rules, and approved sources. <br>
Mitigation: Provide an up-to-date compliance profile and knowledge base, and require human confirmation before marking the review complete. <br>
Risk: The generated report may contain incorrect or misleading compliance guidance if source evidence is missing or ambiguous. <br>
Mitigation: Treat missing sources as unverifiable, review the generated report path, and have a qualified reviewer confirm findings before publication decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-compliance-reviewer) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, files, guidance] <br>
**Output Format:** [Markdown review report saved to content/drafts/{original-name}-compliance-review.md] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not modify the original draft; includes issue locations, suggested fixes, citation verification, overall assessment, approval level, and execution summary.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
