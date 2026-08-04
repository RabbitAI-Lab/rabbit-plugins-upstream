## Description: <br>
Query redfin.com from a shell with the fpx CLI to resolve locations and addresses, search for-sale listings, read property details, retrieve market trends and comparable rentals, inspect climate risk and photos, and access signed-in saved homes or saved searches through a paired browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to produce shell commands and parsing guidance for querying Redfin data through fpx when they need property, listing, market, rental, climate, photo, saved-home, or saved-search information without running the Redfin MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to read private Redfin account data from saved homes or saved searches when the paired browser tab is signed in. <br>
Mitigation: Use saved-home and saved-search examples only when that account-specific access is intended, and avoid saving or sharing command output that contains private results. <br>
Risk: The skill depends on pairing fpx/Transporter with a Redfin browser tab, which extends agent actions through an authenticated browser context. <br>
Mitigation: Install and use the skill only when browser-paired Redfin access is acceptable for the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin-fpx) <br>
- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON parsing examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may describe browser-paired fpx calls and may include guidance for signed-in Redfin account data when explicitly requested.] <br>

## Skill Version(s): <br>
0.10.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
