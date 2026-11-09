## Description:

Analyzes cat and dog images or videos to estimate breeds and distinguish individual pets in multi-pet households.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners can submit pet images or videos for breed and individual-pet analysis, then view associated historical reports. The skill is intended for pet-interest use; its documentation says professional organizations should be used for purebred certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet report histories may be mixed across users if sender isolation is not fixed.

Mitigation: Wait for sender-isolation fixes and review report ownership before relying on or sharing history results.

Risk: The --export-env-only option may not reliably limit execution to environment setup.

Mitigation: Do not rely on that option until its behavior is fixed; avoid using it in shared workspaces.

Risk: Credentials may be retained with insufficient protection.

Mitigation: Avoid supplying unrelated secrets and request clear credential-storage controls before use.

Risk: Household media is sent to LifeEmergence cloud analysis, service charges may apply, and server-side deletion and access controls are unconfirmed.

Mitigation: Only submit media intended for this analysis, confirm registration and deletion controls with the provider, and account for possible service charges.

## Reference(s):

- [API interface reference](references/api_doc.md)
- [LifeEmergence skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [JSON analysis results; Markdown tables for historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pet count, breed and individual-pet findings, confidence, notes, and report links; detail can be basic, standard, or JSON.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release; artifact SKILL.md frontmatter lists 1.0.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
