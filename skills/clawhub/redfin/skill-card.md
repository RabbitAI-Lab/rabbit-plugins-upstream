## Description:

Look up Redfin real-estate listings, property details, market reports, mortgage calculations, and saved Redfin homes or searches through the redfin-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Redfin listing searches, property details, housing-market metrics, mortgage estimates, and saved Redfin homes or searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a signed-in browser bridge whose broad extension permissions are not clearly disclosed in the submitted skill text.

Mitigation: Install only if the user trusts both redfin-mcp and fetchproxy, review the extension permissions, and keep the bridge paired only with MCPs the user intends to use.

Risk: Requests can access saved Redfin homes and saved searches through the user's active browser session when those tools are invoked.

Mitigation: Use saved-home and saved-search requests only when account-specific data is intended, and disable or unpair the browser bridge when not needed.

Risk: Redfin requests rely on private web endpoints and a live browser session, so challenges or site changes can affect results.

Mitigation: Verify important real-estate or financial decisions against Redfin directly and treat agent output as assistive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [fetchproxy browser bridge](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with listing data, market metrics, mortgage breakdowns, and setup snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Redfin outputs; saved-home and saved-search tools depend on the user's signed-in browser session.]

## Skill Version(s):

0.10.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
