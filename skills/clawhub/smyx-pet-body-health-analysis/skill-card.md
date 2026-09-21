## Description:

Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states, helping pet owners detect health issues promptly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners and developers use this skill to analyze pet images or videos for body condition, skin abnormalities, injuries, mental-state indicators, and related health-risk signals. It can also return structured reports, report links, and historical report listings from the configured cloud API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media, identity values, tokens, or account-linked history may be exposed when development or plaintext HTTP endpoints are used.

Mitigation: Install only after the publisher removes development configuration, enforces HTTPS-only allowlisted endpoints, and documents identity, token, and cloud-history handling; avoid private media until then.

Risk: Pet health analysis may be interpreted as a veterinary diagnosis.

Mitigation: Use results as screening and reference information only, and consult a qualified veterinarian when abnormalities are detected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown or JSON pet health analysis report with status text and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local media paths or media URLs; documented outputs include structured analysis reports, historical report tables, and optional saved result files.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter declares 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
