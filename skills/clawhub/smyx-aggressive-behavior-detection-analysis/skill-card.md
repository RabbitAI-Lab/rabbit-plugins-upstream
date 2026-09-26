## Description:

Analyzes livestock and poultry images or barn videos for fighting, biting, chasing, and butting, and reports behavior, intensity, and alert levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock producers and monitoring teams use this skill to flag potentially aggressive behavior in barn footage, review alert levels, and retrieve past analysis reports. Results are for warning and review, not intervention advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting barn footage or URLs sends content to the lifeemergence.com analysis service, potentially including sensitive facility or worker imagery.

Mitigation: Submit only authorized footage and URLs; avoid sensitive imagery and review applicable sharing policies before use.

Risk: The skill creates or reuses a workspace identity, stores service tokens locally, and can retrieve cloud history reports.

Mitigation: Use an isolated workspace, limit access to its stored data, and review or clear the local data database when uninstalling.

## Reference(s):

- [Aggressive behavior detection API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [JSON analysis results or Markdown report tables; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior, intensity, and alert levels; history lists can link to full reports.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
