## Description:

Generates supplier-name matching guidance, compares a bundled sample pair, saves a local match report, and optionally submits results to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and developers can use this skill to explore supplier-name matching guidance and review a local sample match report before adapting it to their own records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runner matches a bundled sample rather than real supplier records.

Mitigation: Treat results as sample output until matching against your own supplier data has been confirmed.

Risk: A configured external destination can receive match results and local artifact paths.

Mitigation: Leave delivery unconfigured unless you intend to share these details; review the destination and data before enabling it.

## Reference(s):

- [Supplier Name Resolution Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-name-resolution-complete)

## Skill Output:

**Output Type(s):** [Guidance, Files]

**Output Format:** [JSON response and local JSON match report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local artifact receipt and a delivery receipt when run; external delivery is optional.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
