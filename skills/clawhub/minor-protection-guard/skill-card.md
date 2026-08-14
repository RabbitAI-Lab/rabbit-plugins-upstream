## Description:

Minor Protection Guard is a local Chinese-language compliance guard that checks product copy, feature descriptions, user agreements, and operating language for six common minor-protection risk patterns before release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT

## Use Case:

Developers, product teams, and compliance reviewers use this skill to screen Chinese product text for minor-protection risk language before publishing network products, games, live-streaming, social, or education experiences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword-based screening can produce false negatives or false positives for minor-protection compliance.

Mitigation: Use findings as a pre-publication triage signal and route important decisions through human legal or compliance review.

Risk: A clean result does not prove that the underlying product implements real-name, anti-addiction, consent, or content-filtering controls.

Mitigation: Verify the actual product controls separately before launch, especially for services directed at or accessible to minors.

## Reference(s):

- [Skill source README](artifact/README.md)
- [Skill source definition](artifact/SKILL.md)
- [Release changelog](artifact/CHANGELOG.md)
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/minor-protection-guard)
- [ClawHub publisher profile](https://clawhub.ai/user/wwumit)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include risk level, category, matched term, legal basis, suggestion, and character offsets when JSON output is requested.]

## Skill Version(s):

1.0.0 (source: package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
