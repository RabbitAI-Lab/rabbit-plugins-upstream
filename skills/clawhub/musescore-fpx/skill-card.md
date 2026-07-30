## Description: <br>
Query musescore.com sheet music search, score and license metadata, and official download links from a shell with the fpx CLI through a signed-in browser tab instead of running the musescore-mcp server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to retrieve MuseScore search results, score metadata, license information, render asset links, and download URLs from shell workflows without running the MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests run through a browser-tab bridge, so misuse could involve account-scoped browser context rather than only anonymous MuseScore lookup data. <br>
Mitigation: Keep the fpx profile scoped to musescore.com and use the skill only for the documented search, metadata, render asset, and download URL resolution flows. <br>
Risk: MuseScore download links may point to gated or paid content even when a URL can be resolved. <br>
Mitigation: Check is_free or hasAccess before relying on a download URL, review MuseScore's terms, and avoid automating purchases or account-only data. <br>
Risk: The skill can resolve download URLs but cannot fetch score files directly through fpx. <br>
Mitigation: Open resolved download URLs manually in the signed-in MuseScore browser tab when access is permitted. <br>


## Reference(s): <br>
- [MuseScore endpoints for fpx](references/endpoints.md) <br>
- [MuseScore JSON store extractor](references/extract-store.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JavaScript helper code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is scoped to anonymous MuseScore search, metadata, render asset lookup, and download URL resolution; fpx cannot download score bytes directly.] <br>

## Skill Version(s): <br>
0.15.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
