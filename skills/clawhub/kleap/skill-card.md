## Description: <br>
Ship a live website or web app end-to-end -- hosting, database, auth, forms, custom domain -- driven from this agent via the kleap CLI (npx, no install). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kleap](https://clawhub.ai/user/kleap) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create, edit, publish, verify, and connect domains for live Kleap-hosted websites and web apps through the Kleap CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, edit, publish, or connect domains for live Kleap-hosted sites in the authenticated account. <br>
Mitigation: Confirm the intended Kleap account, target app, and domain before running create, edit, publish, or domain-connect commands; only report a live URL after the CLI confirms it. <br>
Risk: KLEAP_API_KEY and cached tokens in ~/.kleap/config.json grant account access for headless or repeated CLI use. <br>
Mitigation: Treat API keys and cached tokens as sensitive secrets, avoid logging them, and prefer auth status checks that do not print account secrets. <br>
Risk: Build failures or publish refusals can leave requested changes unpublished even though a previous site version may remain live. <br>
Mitigation: Use the CLI error message to guide at most two fix-and-retry attempts, then report the exact failure instead of claiming the requested change is live. <br>


## Reference(s): <br>
- [Kleap MCP homepage](https://kleap.co/mcp) <br>
- [Kleap ClawHub listing](https://clawhub.ai/kleap/skills/kleap) <br>
- [Kleap recipes](references/recipes.md) <br>
- [Kleap troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise status guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return human-readable lines or JSON when --json is used; successful live-site actions should be confirmed before reporting a URL.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
