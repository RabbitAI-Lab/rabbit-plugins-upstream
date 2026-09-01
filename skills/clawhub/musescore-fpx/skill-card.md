## Description:

Query musescore.com for sheet music search, score and license metadata, and official download-link resolution from a shell with the fpx CLI through a signed-in browser tab, without running the musescore-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable MuseScore users use this skill to search MuseScore, inspect score and license metadata, and resolve official download URLs from shell workflows using a browser-backed fpx profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a persistent fpx browser profile and Transporter extension access to musescore.com.

Mitigation: Install and pair fpx only in environments where that browser bridge and scoped site access are acceptable.

Risk: Resolved download links may point to paid or account-gated MuseScore content.

Mitigation: Review MuseScore terms and confirm is_free or hasAccess before using a resolved download link.

Risk: The fpx path can resolve official download URLs but cannot fetch score bytes from the shell.

Mitigation: Open resolved links manually in the signed-in browser tab when downloads are allowed.

## Reference(s):

- [MuseScore endpoints for fpx](references/endpoints.md)
- [MuseScore JSON-store extractor](references/extract-store.js)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON/jq projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a paired fpx Transporter profile and a musescore.com browser tab that has cleared the site challenge.]

## Skill Version(s):

0.16.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
