## Description:

Read Angi public directory pages from a shell to find service pros, inspect ratings and reviews, and list trade and city taxonomy using the fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch and parse Angi directory pages from a browser-cleared session, rank or filter home-service providers, inspect reviews, and validate trade and city URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install and persistently pair an unpinned browser-bridge CLI.

Mitigation: Install only after trusting @fetchproxy/cli and the Transporter extension, and pin or verify the CLI version where possible.

Risk: Pairing a signed-in my.angi.com tab can expose account pages to fetch commands.

Mitigation: Pair only the specific Angi subdomain needed, avoid my.angi.com unless signed-in account reads are intended, and revoke pairing when finished.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](artifact/references/angi-pages.md)
- [Angi RSC flight extractor](artifact/references/rsc.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, JavaScript, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce JSON arrays parsed from Angi pages when run by an agent.]

## Skill Version(s):

0.3.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
