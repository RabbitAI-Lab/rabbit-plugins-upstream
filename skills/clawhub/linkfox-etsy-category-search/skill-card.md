## Description: <br>
Searches locally synchronized Etsy category data by keyword to retrieve category names, ids, parent ids, and parentIds for product or shop filtering workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to find Etsy category identifiers from synchronized LinkFox category data before passing those ids into Etsy product or shop search tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a LinkFox API key and can send lookup requests to the LinkFox tool gateway. <br>
Mitigation: Install only when LinkFox is trusted, scope the API key to the needed use, and review or constrain the configured gateway before use. <br>
Risk: The helper script writes full responses and cache data to local linkfox folders, which may expose lookup results in the workspace or fallback locations. <br>
Mitigation: Run it only in appropriate workspaces, inspect generated linkfox folders, and remove cached or response files that should not persist. <br>
Risk: The authentication fallback can guide the agent to install a separate onboarding skill from a remote ZIP. <br>
Mitigation: Require explicit manual approval and review the remote onboarding package before installing any additional skill. <br>


## Reference(s): <br>
- [API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-category-search) <br>
- [LinkFox Tool Gateway](https://tool-gateway.linkfox.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with optional shell commands and JSON API responses or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script writes full lookup responses and cache files under local linkfox folders and prints either the full JSON response or a compact summary.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
