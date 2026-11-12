## Description:

Analyzes images or videos of dog toileting areas to describe stool color, shape, blood, and mucus observations in a structured report, without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and pet-care operators use the skill to review images or videos from dog toilets or outdoor walking routes and receive standardized observations of stool appearance and possible abnormalities. It can also retrieve prior analysis reports; the observations are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags undeclared account and report-history features, identity handling, and export-mode behavior that may still trigger analysis or report retrieval.

Mitigation: Review the skill's account, history, and export behavior before use, and confirm that each action is intended for the deployment.

Risk: The security guidance identifies transmission of media and identity data to a remote service, plus local storage of profile information and tokens.

Mitigation: Use only approved media and identity data, and protect the local profile and token storage according to the deployment's access controls.

Risk: The Skillspector scan was partial because a referenced local path was missing; the separate AIG scan had no findings but does not resolve the concerns above.

Mitigation: Review the missing path and complete a full security review before relying on the scan results.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pet-stool-morphology-recognition-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured stool observation report or report list, as text, JSON, or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include color, shape, blood or mucus observations, abnormality prompts, and report links; no disease diagnosis.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
