## Description:

Analyzes reptile enclosure feeding videos for prey attacks, swallowing, feeding refusal, and regurgitation, and reports possible feeding anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and enclosure operators use feeding videos to track attacks, swallowing, refusal, and regurgitation, and to review past anomaly reports. The results are behavior observations, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure footage, supplied URLs, identity metadata, and report history requests are sent to a remote service.

Mitigation: Review before installing; avoid sensitive household footage and share only media and URLs you are comfortable sending to the configured service.

Risk: The skill silently creates or reuses an identity and stores service tokens locally.

Mitigation: Run in an isolated workspace and prefer a release that clearly discloses account behavior and avoids local token storage.

Risk: Python import-path handling may expose execution to untrusted local code.

Mitigation: Use an isolated workspace and prefer a release that fixes the import-path handling.

## Reference(s):

- [Skill API and analysis reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown report or history table; optional JSON or saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports feeding events and alerts; not a veterinary diagnosis.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
