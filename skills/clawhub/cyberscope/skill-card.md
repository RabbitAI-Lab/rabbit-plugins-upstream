## Description:

CyberScope is an offline, zero-dependency Python CLI that lets agents search, inspect, validate, and export a public reference catalog of cyberattack, surveillance, censorship, and defensive methods with cited sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, researchers, educators, and journalists use this skill to retrieve concise public-source references for cyber, surveillance, censorship, and defensive methods without network access or local service dependencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The catalog covers dual-use cyber, surveillance, and censorship methods and could be misused for unauthorized attack planning, surveillance, censorship, disruption, or target selection.

Mitigation: Use the skill only as a lawful research, education, journalism, threat-modeling, or defensive reference, and do not convert catalog entries into operational instructions.

Risk: The source verifier performs static URL checks only and does not prove that links are live or that referenced pages still support a topic.

Mitigation: Open and verify cited resources independently when accuracy, attribution, or current availability matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/cyberscope)
- [Catalog Schema](references/catalog_schema.md)
- [Search Scoring](references/search_scoring.md)
- [Source Verification](references/source_verification.md)
- [Freedom on the Net](https://freedomhouse.org/report/freedom-net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [JSON CLI responses, deterministic JSON/CSV/Markdown exports, and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline and deterministic; read-only except when the export command is given an explicit output directory.]

## Skill Version(s):

2.0.1 (source: server release metadata; artifact frontmatter and changelog report 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
