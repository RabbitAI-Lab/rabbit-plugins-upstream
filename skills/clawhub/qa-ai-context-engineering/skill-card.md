## Description: <br>
Packages completed QA analysis, including requirement breakdowns, scenario trees, boundary lists, and risk assessments, into a structured AI context package for downstream test-case generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers and test architects use this skill after requirement analysis and scenario modeling to assemble a complete business, functional, and technical context package before generating test prompts or test cases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded requirement files or fetched URLs may contain sensitive or untrusted content. <br>
Mitigation: Review inputs before use, avoid including secrets, and treat fetched content as untrusted until checked. <br>
Risk: Incomplete upstream analysis can lead to assumptions in the generated context package. <br>
Mitigation: Review the context package before test-case generation and fill missing upstream analysis when assumptions affect coverage or risk. <br>


## Reference(s): <br>
- [Output Template](references/output-template.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-ai-context-engineering) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown context package with labeled sections and traceability fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Carries upstream requirement IDs and scenario IDs; labels provided, inferred, and assumed information when inputs are incomplete.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
