## Description: <br>
Track your Product Hunt launch stats (Rank, Upvotes, Comments) in real-time via CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abakermi](https://clawhub.ai/user/abakermi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, founders, and launch teams use this skill to check Product Hunt post stats, monitor launch progress, and list the current leaderboard from the terminal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a Product Hunt API token. <br>
Mitigation: Use a limited Product Hunt developer token, keep it out of committed files and logs, and revoke it if it is no longer needed. <br>
Risk: The skill calls an external ph-launch CLI command. <br>
Mitigation: Confirm that ph-launch is the trusted Product Hunt CLI you intend to use before installing or running commands. <br>


## Reference(s): <br>
- [Product Hunt API Dashboard](https://www.producthunt.com/v2/oauth/applications) <br>
- [ClawHub Skill Page](https://clawhub.ai/abakermi/skills/product-hunt-launch) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/abakermi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the PH_API_TOKEN environment variable and an external ph-launch CLI command.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
