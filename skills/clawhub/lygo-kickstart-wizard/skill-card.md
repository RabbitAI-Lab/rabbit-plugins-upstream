## Description:

LYGO Kickstart Wizard provides plain-English onboarding for the ClawHub lattice by mapping ecosystem tools, checking public lattice health, analyzing text for ops signals through an optional local detector, and guiding mint-verify-anchor workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

External users, developers, and operators use this skill to find an appropriate LYGO or ClawHub next step without reading source code first. It supports onboarding, ecosystem mapping, fixed-endpoint lattice health checks, local text-analysis routing, and guided mint-verification planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The lattice command makes network requests.

Mitigation: Network use is limited to HTTPS GET requests against fixed public endpoints for the lattice health intent.

Risk: Text analysis or file hashing can process user-provided paths or sensitive text.

Mitigation: Use only text and files the operator is authorized to provide; reads are limited to explicit --text-file or --pack paths.

Risk: The optional write mode can create or overwrite a local report path.

Mitigation: Write output only to intended locations and require both --write and --i-consent before writing.

Risk: Optional ops-detector use may be mistaken for a personal verdict.

Mitigation: Treat analysis as local signal guidance, not a person verdict, and avoid private third-party text without authority.

## Reference(s):

- [LYGO Kickstart Wizard ClawHub listing](https://clawhub.ai/deepseekoracle/skills/lygo-kickstart-wizard)
- [DeepSeekOracle publisher profile](https://clawhub.ai/user/deepseekoracle)
- [OpenClaw homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-kickstart-wizard)
- [LYGO adoption roadmap](references/ROADMAP.md)
- [Security notes](references/SECURITY.md)
- [SkillSpector audit](references/SKILLSPECTOR_AUDIT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally write a local report only when --write is paired with --i-consent.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, claw.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
