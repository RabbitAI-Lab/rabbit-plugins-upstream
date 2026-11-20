## Description:

Helps Hermes agents use independent model perspectives to review consequential architecture, product, and implementation decisions through deliberations, design reviews, and pressure tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

Hermes users and developers use mumo when consequential architecture, design, or product decisions would benefit from independent model perspectives. It supports design and plan review, pre-launch pressure tests, adversarial review, and decisions with meaningful tradeoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User context may be sent to external model providers without a clear privacy check.

Mitigation: Review and minimize prompt content; omit confidential or identifying information unless its use with external providers is approved.

Risk: Security scan evidence is limited because Skillspector reported an exit-status error.

Mitigation: Treat the scan as incomplete and review the skill's data handling before installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ericatmumo/skills/mumo-hermes)
- [mumo MCP documentation](https://mumo.chat/docs/mcp)
- [mumo API documentation](https://mumo.chat/docs/api)
- [Hermes install guide](https://mumo.chat/install/hermes)
- [mumo product](https://mumo.chat)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Model responses with typed reactions and a claim map, followed by a Markdown synthesis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses reflect multiple model perspectives; no fixed token cap is stated.]

## Skill Version(s):

0.7.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
