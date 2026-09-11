## Description:

Discover locally running HTTP interfaces, identify their listening ports and processes, and build a browsable launcher dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to find local dashboards, notebooks, previews, and development servers that are currently responding over HTTP. It helps produce a current launcher view with ports, process metadata, page titles, response status, and links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner can record sensitive local service inventory, including page titles, ports, process names, and PIDs, in a persistent dashboard file.

Mitigation: Review or delete ~/.local/state/local-uis/dashboard.html before sharing the machine, workspace, or generated output.

Risk: The local-only scanning boundary is not a complete network-isolation guarantee because redirects and standard proxy handling may affect HTTP requests.

Mitigation: Run the skill only where probing local services is authorized, and avoid sensitive network environments until redirects are constrained to loopback.

Risk: The scanner opens the generated dashboard by default, which may expose discovered service metadata on screen.

Mitigation: Use --no-open when browser launch is not desired.

## Reference(s):

- [Local UIs ClawHub Page](https://clawhub.ai/antreasantoniou/skills/local-uis)
- [README](README.md)
- [Skill Instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, code]

**Output Format:** [Terminal text, optional JSON, and a generated HTML dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dashboard is written to ~/.local/state/local-uis/dashboard.html and may be opened automatically unless --no-open is used.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
