## Description: <br>
Query and manage OpenTable (opentable.com) restaurant reservations from a shell with the fpx CLI (@fetchproxy/cli) instead of running the opentable-mcp server; search restaurants, check slot availability, list reservations/favorites, and book, modify, or cancel a table via one-shot GraphQL and REST calls through a signed-in browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to script OpenTable search, availability, profile, favorites, booking, modification, and cancellation workflows through a signed-in browser session when the OpenTable MCP server is unavailable or unnecessary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform real OpenTable reservation, modification, cancellation, and favorites actions through the user's signed-in browser session. <br>
Mitigation: Use the documented preview and booking-details steps to inspect cancellation policies, card requirements, dining area IDs, and reservation details before running write commands. <br>
Risk: The workflow gives fpx and Transporter access to a signed-in OpenTable session. <br>
Mitigation: Install and use it only when comfortable granting that session access, and keep the browser tab, pairing state, and site access limited to the intended OpenTable workflow. <br>


## Reference(s): <br>
- [OpenTable requests for fpx](references/opentable-fpx-requests.md) <br>
- [OpenTable initial state extractor](references/extract-initial-state.mjs) <br>
- [OpenTable](https://www.opentable.com) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for execution through a signed-in OpenTable browser session via fpx and may include immediate account-changing write calls.] <br>

## Skill Version(s): <br>
0.16.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
