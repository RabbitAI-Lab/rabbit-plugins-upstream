## Description: <br>
FSB drives the user's Chrome via the FSB extension and an MCP bridge for live web tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lakshmanturlapati](https://clawhub.ai/user/lakshmanturlapati) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use FSB when an agent must operate a real Chrome session for clicks, typing, multi-tab flows, logged-in reads, or pages whose useful state depends on JavaScript or browser cookies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate the user's real Chrome session, including pages with existing cookies, saved auth, or live account state. <br>
Mitigation: Install it only when browser automation is intended, keep visual-session overlays enabled for action calls, and require explicit user confirmation before purchases, payments, account changes, deletions, permission grants, settings writes, or public posts. <br>
Risk: Using npx without a version specifier resolves the latest fsb-mcp-server package at runtime. <br>
Mitigation: Pin fsb-mcp-server to a reviewed version in MCP host configuration when review-before-upgrade is required. <br>
Risk: Host installers can write MCP configuration for detected local clients. <br>
Mitigation: Review every host-config prompt and run only the installers for hosts the user wants configured. <br>
Risk: Passwords, CVVs, or saved payment details could leak if an agent passes secret values through chat or tool arguments. <br>
Mitigation: Use the FSB vault-backed credential and payment flows so secrets remain inside the browser extension and are not echoed into prompts, logs, or MCP arguments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lakshmanturlapati/skills/full-selfbrowsing) <br>
- [Full Self Browsing homepage](https://full-selfbrowsing.com) <br>
- [FSB Chrome extension](https://chromewebstore.google.com/detail/badgafnfchcihdfnjneklogedcdkmjfk) <br>
- [fsb-mcp-server npm package](https://www.npmjs.com/package/fsb-mcp-server) <br>
- [USAGE.md](USAGE.md) <br>
- [Default to FSB](references/default-to-fsb.md) <br>
- [FSB tool decision tree](references/tool-decision-tree.md) <br>
- [Visual session lifecycle](references/visual-session-lifecycle.md) <br>
- [Vault boundary](references/vault-boundary.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON or YAML configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to use MCP browser tools and local diagnostic scripts.] <br>

## Skill Version(s): <br>
0.9.90 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
