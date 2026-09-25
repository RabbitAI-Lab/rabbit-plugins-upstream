## Description:

Analyzes child bedroom night-time audio and video to identify bedtime crying, fear-of-dark behaviors, nightmare awakenings, and out-of-bed events, then returns structured findings and soothing-action guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze child bedroom night-time media, detect signs of distress or unsafe out-of-bed events, and generate structured soothing recommendations, reports, and history views. It is intended for household parenting workflows where parent or guardian consent, privacy controls, and cloud-retention review are in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-bedroom audio and video may be uploaded or passed to cloud services.

Mitigation: Confirm parent or guardian consent, household notice, and the provider's retention, deletion, and sharing policy before installation.

Risk: The skill may create or reuse a hidden local identity and persist authentication tokens.

Mitigation: Review local storage and token-handling behavior, and install only in environments where this persistence is acceptable.

Risk: Device-control claims for lights, speakers, and parent notifications may not match the deployed integration.

Mitigation: Validate integrations in a controlled environment before enabling automated soothing actions or urgent alerts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)
- [API 接口文档](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-backed text reports with command examples and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include event classifications, soothing-action recommendations, history tables, report links, and local output files.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
