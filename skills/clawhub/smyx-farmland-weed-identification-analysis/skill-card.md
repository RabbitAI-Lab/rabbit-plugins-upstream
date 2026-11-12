## Description:

Identifies weed species and estimates coverage density in field images, producing distribution heatmap data to support precision weeding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farmers and agricultural practitioners can submit top-down field images or videos to identify weeds, estimate their distribution and coverage density, and receive structured heatmap data for precision weeding decisions. The results are for field-management reference and do not provide herbicide or treatment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because scanners report account, credential, and history handling beyond its stated weed-analysis purpose.

Mitigation: Before installation, independently review credential handling, destination checks, account creation, and history retrieval, and confirm the declared purpose and tool scope match the behavior.

Risk: The security scan is partial because one local reference was missing, so the artifact's behavior is not fully verified.

Mitigation: Review the missing reference and complete an independent review before installation.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill introduction demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Heatmap data]

**Output Format:** [Structured JSON analysis results and Markdown report lists with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include weed species, distribution areas, coverage-density levels, a field weed-pressure level, heatmap data, and report links.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
