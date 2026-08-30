## Description:

LYGO Site Card turns a public HTTPS URL or local HTML file into a compact identity card with title, description, canonical URL, selected security headers, companion files, SHA-256, and ALIGNED/DRIFT/SHADOW status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers, operators, and agents use this skill to check whether public pages are live, inspect CSP/HSTS-related header posture, compare staging and production pages, or parse local HTML without making a network request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill on pages the operator is not authorized to inspect could create inappropriate scanning behavior.

Mitigation: Use it only for public web pages you are authorized to request; the skill blocks non-HTTPS, loopback, private, link-local, reserved, and redirected private hosts.

Risk: Saved reports or local HTML parsing can expose metadata from sensitive content.

Mitigation: Use --write only with explicit consent and intended output paths, and avoid --file on sensitive private HTML unless printing or saving its metadata is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-site-card)
- [ClawHub package link](https://clawhub.ai/deepseekoracle/lygo-site-card)
- [Project homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-site-card)
- [Security reference](references/SECURITY.md)
- [SkillSpector audit notes](references/SKILLSPECTOR_AUDIT.md)
- [Quickstart](examples/quickstart.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Files]

**Output Format:** [JSON printed to stdout, with optional JSON file output when --write and --i-consent are provided]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports card, headers, and compare modes; URL mode uses HTTPS GET for public hosts, and --file parses local HTML without network access.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
