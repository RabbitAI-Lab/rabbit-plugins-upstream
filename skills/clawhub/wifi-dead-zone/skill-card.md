## Description:

Use when Wi-Fi is slow or drops in specific rooms, when placing a router or mesh node in a new home, when deciding if you need a mesh system or just a better router spot, when your 5 GHz doesn't reach the bedroom, or when picking clean channels among neighbors - builds a floor plan of your home as a simple model, estimates per-room signal with RF path loss and wall attenuation, renders an ASCII heatmap, searches candidate router spots, guides mesh placement, calibrates against phone measurements, and recommends non-overlapping channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to model home Wi-Fi coverage from room, wall, router, and measurement data, then decide where to place routers or mesh nodes and which channels to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool can update a user-provided home JSON file when survey measurements are recorded.

Mitigation: Keep a backup of important home files and pass only the intended Wi-Fi home file to --home.

Risk: Planning-grade RF estimates may miss furniture, people, appliances, or transient interference.

Mitigation: Use survey and compare measurements before buying hardware or making permanent placement decisions.

Risk: Using the model for enterprise deployment, outdoor bridging, or ISP disputes could overstate its precision.

Mitigation: Use it for home planning only and rely on professional site surveys or measurement tools for higher-stakes cases.

## Reference(s):

- [Home File Guide](references/home-file-guide.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/wifi-dead-zone)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local Wi-Fi planning guidance, ASCII heatmaps, tabular signal estimates, router and mesh placement recommendations, channel recommendations, and home-file configuration updates.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
