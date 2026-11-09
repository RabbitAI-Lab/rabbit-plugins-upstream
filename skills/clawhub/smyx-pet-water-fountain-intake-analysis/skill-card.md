## Description:

Analyzes pet water-fountain videos to estimate drinking frequency, session duration, and daily intake, compare results with historical baselines, and flag notable changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and animal-care teams use the skill to review fountain footage, track each pet’s estimated water intake over time, and spot changes that may warrant attention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video files or their URLs may be uploaded to lifeemergence.com services, including through the “export only” option.

Mitigation: Avoid private footage until the upload behavior is corrected; review footage and URLs before submitting them.

Risk: Windows HTTP logging may expose sensitive data, and account tokens are retained locally.

Mitigation: Protect the workspace database and confirm how to remove local credentials and cloud reports; avoid private footage until logging is fixed.

Risk: Authenticated requests may reach destinations that are not trusted HTTPS hosts.

Mitigation: Restrict authenticated requests to trusted HTTPS destinations before use.

Risk: Service-side retention, access controls, and analysis accuracy could not be established from the release bundle.

Mitigation: Confirm the service’s data practices and treat estimates as monitoring aids rather than diagnostic results.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference notes](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured text or JSON reports; Markdown tables for historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intake is estimated from observed drinking behavior; results are not direct measurements or medical diagnoses.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
