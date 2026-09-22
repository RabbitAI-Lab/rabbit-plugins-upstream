## Description:

A zero-dependency, plug-and-play interactive PRD annotation and multi-version specification framework for HTML, Vue, and React prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barry0-0](https://clawhub.ai/user/barry0-0)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, UX designers, and frontend developers use this skill to add in-page PRD pins, rich Markdown specifications, versioned requirements, and exportable PRD documents to existing prototypes. It supports static HTML prototypes and framework-aware integration guidance for Vue and React projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release stores powerful cloud or GitHub write credentials in browser storage.

Mitigation: Use narrowly scoped, disposable credentials; avoid confidential PRD data until credential storage is redesigned; rotate any credentials used during testing.

Risk: The bundled local write server is unauthenticated and uses permissive CORS.

Mitigation: Run the server only on localhost or a trusted machine; do not expose it to a network; add authentication and restrictive CORS before team or hosted use.

Risk: The scanner flagged exploitable rendering weaknesses around Markdown rendering.

Mitigation: Sanitize rendered Markdown and HTML, and review imported or externally supplied PRD content before displaying it in shared prototypes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/barry0-0/skills/pm-proto-prd-pin)
- [Publisher profile](https://clawhub.ai/user/barry0-0)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and generated or modified project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PRD annotation assets, local server commands, persistence configuration, and exportable Markdown, JavaScript data, or PDF-ready PRD documents.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
