## Description:

Supports uploading local MP4 videos or network video URLs to call a server-side API for facial diagnosis and return structured TCM facial diagnosis results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit consented local videos or public video URLs for TCM-style facial analysis, structured health-reference results, recommendations, report links, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send facial videos or supplied video URLs to a remote Life Emergence service for health-style analysis.

Mitigation: Use only with non-sensitive, consented media and review remote service terms, data handling, and endpoint scope before production or regulated use.

Risk: Report history may be associated with an automatically managed local or cloud identity.

Mitigation: Confirm user identity handling, retention expectations, and history-query behavior before enabling the skill for shared or sensitive environments.

Risk: The security verdict is suspicious because service tokens may persist without clear user control.

Mitigation: Review token storage, rotation, and deletion controls before deployment, and avoid use where persistent identity tokens are not acceptable.

Risk: The skill provides TCM-style health analysis that could be mistaken for medical diagnosis.

Mitigation: Present outputs as informational health references only and require professional medical review for diagnosis or treatment decisions.

Risk: Dependency versions are not fully pinned across all requirements files.

Mitigation: Pin and audit dependencies in the deployment environment before production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-face-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](artifact/references/api_doc.md)
- [Shared API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis results with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured facial-analysis results, health-reference suggestions, historical report lists, and remote report image links.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
