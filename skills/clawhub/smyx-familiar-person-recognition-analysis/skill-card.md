## Description:

Analyzes images and videos against an enrolled face database to identify familiar people and produce recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home and workplace operators can use the skill to compare submitted images or videos with an enrolled acquaintance face database. It returns recognition results and links to reports, and can list historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the no-analysis option is ignored, which can result in analysis running when it was meant to be disabled.

Mitigation: Have the option corrected and verified before use.

Risk: The security review flags unsafe credential-as-identity behavior and account creation without clear control.

Mitigation: Correct credential handling, require explicit control over account creation, and protect the local token database.

Risk: Submitted facial media raises authorization, retention, and deletion concerns.

Mitigation: Obtain authorization for submitted footage and confirm the provider's facial-media retention and deletion terms.

## Reference(s):

- [API interface reference](artifact/references/api_doc.md)
- [API errors reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Files]

**Output Format:** [Structured JSON analysis reports; Markdown tables for report history, with optional file output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local files or URLs for images and videos; reports recognition results, recommendations, and report links.]

## Skill Version(s):

1.0.19 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
