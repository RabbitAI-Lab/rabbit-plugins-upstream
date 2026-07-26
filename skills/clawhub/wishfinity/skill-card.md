## Description: <br>
Add "save for later" to shopping agents, product recommendation engines, gift idea generators, and AI commerce experiences by saving product URLs to a universal Wishfinity wishlist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leebellon](https://clawhub.ai/user/leebellon) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers building shopping agents, product recommendation engines, gift idea generators, and AI commerce experiences use this skill to offer a user-facing save-for-later action that sends product URLs to Wishfinity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on Wishfinity and the wishfinity-mcp-plusw npm package. <br>
Mitigation: Install it only when the deployment trusts Wishfinity and the npm package, and review the package before production use. <br>
Risk: Product URLs can contain private tokens, account-specific identifiers, or other sensitive query parameters. <br>
Mitigation: Use confirmation for ambiguous save requests and avoid sending URLs that include sensitive parameters. <br>


## Reference(s): <br>
- [Wishfinity](https://wishfinity.com) <br>
- [Wishfinity MCP server](https://github.com/wishfinity/wishfinity-mcp-plusw) <br>
- [ClawHub skill page](https://clawhub.ai/leebellon/skills/wishfinity) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration and MCP tool output fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The MCP tool add_to_wishlist accepts a product URL and returns an action_url plus display_text for the user-facing save flow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
