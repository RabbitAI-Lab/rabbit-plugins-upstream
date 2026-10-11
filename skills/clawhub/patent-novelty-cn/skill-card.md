## Description:

Helps assess a technical invention against published prior art and produces a comparison-based novelty report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, researchers, and patent teams use this skill to screen an invention before filing or project review, compare its technical features with published sources, and obtain a scoped novelty assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Technical descriptions sent to PatentMax may disclose confidential or unfiled invention details.

Mitigation: Obtain authorization before sending sensitive material; omit trade secrets or unfiled core parameters when disclosure is not approved.

Risk: Locally stored trial credentials or the PATENTMAX_API_KEY environment variable may be exposed on shared systems.

Mitigation: Restrict access to credentials and remove cached trial keys from shared systems when no longer needed.

Risk: Paid searches can incur charges, including for repeated runs with changed inputs.

Mitigation: Confirm cost and obtain user approval before execution; check an existing operation's status instead of submitting it again.

Risk: Incomplete publication coverage or search terms can produce an overconfident patentability conclusion.

Mitigation: State the search scope and limitations, verify cited publications, and seek a qualified professional assessment for formal decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-novelty-cn)
- [Technical solution guide](references/solution-guide.md)
- [Patent novelty workflow](references/workflow.md)
- [FAQ and troubleshooting](references/faq.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown analysis with optional DOCX report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites comparison documents and qualifies conclusions by search coverage and data quality.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
