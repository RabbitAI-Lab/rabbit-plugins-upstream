## Description:

Find published Namegarage domains, look up listing details, compare payment options, and suggest alternatives when a user is choosing a domain for a project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[namegarage](https://clawhub.ai/user/namegarage)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to search Namegarage's published domain listings, review listing details and payment options, and compare alternatives for a project. It provides decision support from public catalog data; it does not establish trademark rights or reserve a name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search text is sent to Namegarage and could contain confidential project details.

Mitigation: Use general project descriptions and omit confidential details unless the user chooses to share them.

Risk: A catalog result does not establish registrar availability, and a listing does not reserve a name; current purchase terms may change.

Mitigation: Check the returned Namegarage page for current availability and terms before making a purchase decision.

Risk: The security scan was only partially complete because two local reference checks were missing.

Mitigation: Treat the clean verdict as limited to reviewed material and use ordinary care while the missing references remain unchecked.

## Reference(s):

- [Namegarage Quickstart](https://namegarage.com/docs/quickstart.md)
- [Namegarage OpenAPI contract](https://namegarage.com/openapi.json)
- [Namegarage developer changelog](https://namegarage.com/developers/changelog/)
- [A2A request guide](https://namegarage.com/docs/a2a.md)
- [Namegarage A2A Agent Card](https://namegarage.com/.well-known/agent-card.json)
- [Namegarage UCP guide](https://namegarage.com/docs/ucp)
- [Namegarage UCP discovery](https://namegarage.com/.well-known/ucp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries and recommendations, with Markdown where appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Based on public catalog results; listings do not reserve names or establish registrar availability.]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
