## Description: <br>
Query musescore.com sheet music search, score and license metadata, and official download-link metadata from a shell with the fpx CLI through a signed-in browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to query MuseScore search results, score metadata, license fields, and official download-link metadata from shell workflows when the MuseScore MCP server is not installed or running. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes scoped musescore.com requests through @fetchproxy/cli and the Transporter browser extension. <br>
Mitigation: Install only if comfortable with that browser bridge and keep extension site access limited to musescore.com. <br>
Risk: The skill can resolve official download URLs but cannot fetch protected score bytes, and download access may depend on MuseScore entitlement. <br>
Mitigation: Open resolved URLs manually in the signed-in browser tab, check is_free or hasAccess before relying on a link, and stay within MuseScore terms and entitlement limits. <br>


## Reference(s): <br>
- [MuseScore endpoints for fpx](artifact/references/endpoints.md) <br>
- [MuseScore JSON store extractor](artifact/references/extract-store.js) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell, JavaScript, and jq examples; commands may produce JSON extracted from MuseScore page data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires @fetchproxy/cli, the Transporter browser extension, and a musescore.com tab with scoped site access.] <br>

## Skill Version(s): <br>
0.15.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
