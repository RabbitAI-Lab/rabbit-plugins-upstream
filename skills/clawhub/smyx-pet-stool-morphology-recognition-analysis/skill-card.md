## Description:

Analyzes pet stool in images or videos from dog toilets or walking paths, reporting visible color, consistency, blood, or mucus without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use this skill to review images or videos of pet stool for observable changes and to retrieve past analysis reports. Results are health observations, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet and household images or videos are sent to lifeemergence.com services for analysis.

Mitigation: Review the media and destination before using the skill; submit only content you are comfortable sharing.

Risk: The skill can silently create or reuse a cloud identity and store authentication tokens in a workspace database.

Mitigation: Review the skill before installation and clear the local database and tokens when you stop using it.

Risk: The skill can automatically retrieve cloud report history.

Mitigation: Use it only if you are comfortable with cloud history access and review stored reports as needed.

## Reference(s):

- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or report-history list; JSON output is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observed stool characteristics, alerts, suggestions, and report links; does not diagnose disease.]

## Skill Version(s):

1.0.8 (source: server release; bundled SKILL.md lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
