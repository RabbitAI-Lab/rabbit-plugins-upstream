## Description:

Assembles a detailed company or project dossier from public sources, tracing every claim to verified evidence through coordinated role workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and due-diligence analysts use this agent configuration bundle to collect public records, assess risk, trace evidence, and draft a sourced company or project dossier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundle includes an unrelated trading-control role with broad external invocation powers.

Mitigation: Remove the risk-officer role or tightly scope it unless connecting the skill to trading or other operational systems is intentional and reviewed.

Risk: Public-source due-diligence dossiers can become misleading if claims are not kept tied to verifiable evidence.

Mitigation: Run the bundled evaluation set before use and require every dossier claim to retain its supporting public-source trace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/due-diligence-team)
- [Artifact skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown dossier and role workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims are expected to be traced to public-source evidence; security evidence flags an unrelated trading-control role for review.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact text states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
