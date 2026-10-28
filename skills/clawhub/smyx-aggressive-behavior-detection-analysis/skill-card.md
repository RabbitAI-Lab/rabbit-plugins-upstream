## Description:

Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing, and butting, and outputs behavior type, intensity level, and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock and poultry farm operators use the skill to screen barn images or videos for aggressive interactions and review structured findings such as behavior type, intensity, alert level, and historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared accounts can expose report histories across users.

Mitigation: Defer shared-user deployment until sender isolation is fixed; use isolated accounts for report access.

Risk: The export-only option may still upload submitted footage to Life Emergence's cloud service.

Mitigation: Treat submitted footage as cloud-uploaded and avoid private footage until enrollment and upload controls are clear.

Risk: Account tokens remain stored locally.

Mitigation: Confirm credential-storage controls before using private footage and restrict access to the local environment holding the account token.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results in JSON or Markdown, including behavior segments, intensity and alert levels; historical report lists are formatted as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts livestock or poultry images and videos, local files, or URLs; documented image/video formats include JPG, PNG, JPEG, MP4, AVI, and MOV, with a 10 MB per-file limit.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
