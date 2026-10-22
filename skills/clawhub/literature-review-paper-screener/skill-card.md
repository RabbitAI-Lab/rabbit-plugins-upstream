## Description:

This skill supports Medical Science literature reviews by gathering and validating paper evidence, submitting it for user-approved cloud screening, and producing audited Paper Sheet and Reading List spreadsheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

MIT

## Use Case:

External researchers and students use the skill to collect, verify, and screen literature for Medical Science reviews, then organize the results into Excel deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Literature searches and paper evidence may include sensitive details, and screening transfers records to a paid third-party cloud service.

Mitigation: Remove personal details from search queries and handoffs, review what will be transferred, and obtain explicit approval for each transfer and its cost.

Risk: The private cloud implementation and required external CLI were not included in the security review.

Mitigation: Install a reviewed CLI version and confirm the destination and processing terms before submitting evidence.

Risk: The documentation contains conflicting upload instructions, and reusing an output folder can risk mixing run artifacts.

Mitigation: Clarify the applicable upload procedure before a run and use a fresh output folder for each run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ez-hq/skills/literature-review-paper-screener)
- [Publisher release metadata (GitHub releases)](https://github.com/ez-hq/literature-review-paper-screener/releases)
- [Architecture reference — Local vs Cloud](references/architecture.md)
- [Evidence package schema](references/evidence-package-schema.md)
- [Metadata validation gate](references/metadata-validation-gate.md)

## Skill Output:

**Output Type(s):** [JSON evidence records, Excel spreadsheets, Plain-language summaries]

**Output Format:** [Per-paper JSON evidence records and Excel Paper Sheet and Reading List workbooks, accompanied by a plain-language summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence availability is recorded per paper (Levels A–D). The bundled MIT license covers local code only; the private cloud template is proprietary and excluded.]

## Skill Version(s):

1.4.9 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
