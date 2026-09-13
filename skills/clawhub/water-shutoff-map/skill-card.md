## Description:

Guides households through locating home water shutoff valves, recording them in a local JSON registry, generating a printable emergency card, and rehearsing first-response steps for leaks or floods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, including homeowners, renters, landlords, and household members, use this skill to find water shutoff valves before an emergency and maintain a durable emergency reference. Agents can use it to guide a shutoff-location workflow, validate the registry, and produce printable household instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local registry and printed card can expose household shutoff locations, contact details, and optional photo paths.

Mitigation: Treat the registry file and printed card as private household safety information and share them only with trusted household members or responders.

Risk: Forcing old, corroded, stuck, shared-building, or municipal valves can create damage or violate local operating rules.

Mitigation: Do not force uncertain valves; call a plumber, landlord, building staff, or utility when a valve is stuck, shared, municipal, or unclear.

## Reference(s):

- [Locating Water Shutoffs - The Hunting Guide](references/locating-shutoffs.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/water-shutoff-map)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/water-shutoff-map)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON registry data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce printable emergency-card text and local registry JSON; no network access is indicated by the security evidence.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
