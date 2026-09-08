## Description:

Analyzes plant leaf images or videos to identify disease lesion features, estimate the likely disease type and confidence, and return a structured report with general prevention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, gardeners, and farm inspectors use this skill to triage plant leaf disease symptoms from images or videos and receive structured diagnostic output. Developers can also invoke the bundled scripts to run analysis, query cloud history, or save report output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags an active private plaintext HTTP development endpoint configuration.

Mitigation: Require the publisher to remove development HTTP/private-IP configuration and document all external destinations before installation.

Risk: The security scan reports silent identity handling and reusable token storage.

Mitigation: Require opt-in for cloud history/account creation and store reusable tokens in a proper secret store rather than a shared workspace database.

Risk: Plant disease classification may be uncertain for blurry images, similar symptoms, or mixed infections.

Mitigation: Present results as diagnostic references, avoid specific chemical treatment instructions, and recommend expert confirmation for severe or ambiguous cases.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Plant Leaf Disease API Documentation](artifact/references/api_doc.md)
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with JSON-like structured analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a user-specified output file; history queries return structured report lists.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
