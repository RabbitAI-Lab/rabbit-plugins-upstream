## Description: <br>
Use the wallapop CLI to search listings, fetch item details, view user profiles, and list categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pjtf93](https://clawhub.ai/user/pjtf93) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to produce correct wallapop-cli commands for searching Wallapop listings, fetching item and user details, listing categories, and requesting JSON output for scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill describes commands that may send search terms, location variables, item lookups, user lookups, and optional access tokens to Wallapop's API. <br>
Mitigation: Install wallapop-cli only from a trusted source, use WALLAPOP_ACCESS_TOKEN only when needed, and avoid sending sensitive locations or tokens unless required for the task. <br>
Risk: The commands require network access and an installed wallapop-cli runtime, so failures may occur if dependencies, API access, or credentials are unavailable. <br>
Mitigation: Confirm Node.js 18+, wallapop-cli installation, network access to api.wallapop.com, and required environment variables before relying on command output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pjtf93/skills/wallapop-cli) <br>
- [Publisher profile](https://clawhub.ai/user/pjtf93) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require wallapop-cli, Node.js 18+, network access to api.wallapop.com, and optional WALLAPOP_ACCESS_TOKEN for non-search endpoints.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
