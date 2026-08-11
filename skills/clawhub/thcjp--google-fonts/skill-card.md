## Description:

Google Fonts指南 helps agents provide Google Fonts selection, pairing, loading optimization, variable font, subsetting, and self-hosting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agent users use this skill to choose Google Fonts, generate font pairing advice, and get implementation guidance for CSS loading, variable fonts, subsetting, and self-hosting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the release suspicious because its declared command execution, file-writing, API, and credential-handling capabilities are broader than needed for Google Fonts advice.

Mitigation: Use the skill for font-related guidance only; do not grant broad automation, command execution, file mutation, or credential access unless a user explicitly reviews and approves the action.

Risk: Generated font-loading or self-hosting guidance may lead to incorrect configuration, privacy exposure, or performance regressions if applied without review.

Mitigation: Review generated CSS, HTML, shell commands, and hosting instructions before applying them, and test font loading, caching, CORS, and regional privacy requirements in the target environment.

Risk: The release has no server-resolved GitHub import provenance for this version.

Mitigation: Treat the ClawHub package and server-resolved publisher metadata as the available provenance, and verify source history separately before high-trust or enterprise deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/google-fonts)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)
- [Google Fonts CSS API](https://fonts.googleapis.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline HTML, CSS, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include font pairing recommendations, CSS snippets, HTML link tags, self-hosting steps, and troubleshooting guidance.]

## Skill Version(s):

1.0.1 (source: server-resolved release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
