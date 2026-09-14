## Description:

Use when Wi-Fi is slow or drops in specific rooms, when placing a router or mesh node in a new home, when deciding if you need a mesh system or just a better router spot, when your 5 GHz doesn't reach the bedroom, or when picking clean channels among neighbors; builds a floor plan of your home as a simple model, estimates per-room signal with RF physics, renders an ASCII heatmap, searches candidate router locations, supports mesh-node guidance, calibrates against phone measurements, and recommends non-overlapping channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and home-network troubleshooters use this skill to model a home's room and wall layout, estimate Wi-Fi signal quality, compare router or mesh placement options, calibrate estimates with local measurements, and choose less crowded channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home layout files and Wi-Fi measurements can reveal private details about a user's residence or network conditions.

Mitigation: Keep home JSON files local, review them before sharing, and install only if comfortable storing this information locally; the security evidence reports no network transmission or background components.

Risk: The RF model is planning-grade and may be inaccurate when walls, furniture, appliances, or interference are not represented correctly.

Mitigation: Use the survey and compare workflow with real measurements before buying hardware or making permanent placement decisions.

## Reference(s):

- [Home File Guide](references/home-file-guide.md)
- [Source repository](https://github.com/voronindenis5/wifi-dead-zone)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/wifi-dead-zone)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASCII heatmaps, per-room signal tables, ranked placement advice, channel recommendations, and local home-file updates when the survey command is used.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
