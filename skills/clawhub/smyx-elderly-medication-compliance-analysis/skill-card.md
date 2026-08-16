## Description:

Monitors medication-area images or videos to identify pick-up, to-mouth, and swallow steps, then returns a structured medication-adherence result and report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and care-system operators use this skill to analyze medication-area footage for visual confirmation of pick-up, to-mouth, and swallow steps. The output supports medication-adherence review and caregiver follow-up, but does not replace medical advice or manual verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Medication-area images or videos may contain sensitive health and household information and are sent to the vendor's cloud service for analysis.

Mitigation: Use only with informed consent from the monitored person or legal caregiver, and confirm the vendor's storage, retention, and access controls before deployment.

Risk: Analysis and history queries are linked to an automatically managed local or user identity with persisted tokens.

Mitigation: Run the skill in a trusted workspace, protect local credential storage, and use an explicit managed identity when the deployment requires account separation.

Risk: History-query output may expose account-linked medication-adherence reports in shared or ambiguous conversations.

Mitigation: Restrict history queries to authorized users and trusted sessions, and verify the requester before displaying report lists or links.

Risk: Visual adherence classification can be incomplete or wrong and is not a medical dosing recommendation.

Mitigation: Treat results as assistive evidence only; manually verify missed-dose alerts and keep clinical decisions with qualified caregivers or clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON text from command-line execution, including structured adherence fields and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the analysis result to a user-specified output file.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
