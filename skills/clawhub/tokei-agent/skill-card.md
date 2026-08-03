## Description: <br>
Tokei (tokei.io) is a pre-launch, waitlist and giveaway platform; this CLI controls launch pages, competition giveaways, sweepstakes, referral and viral-loop campaigns, Product Hunt launch drives, Gleam-style and KickoffLabs-style entry pages, and related campaign data through the Tokei v1 REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gilesdawe](https://clawhub.ai/user/gilesdawe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and AI agents use this skill to manage Tokei pre-launch, waitlist, giveaway, referral, and launch campaigns from a CLI or MCP tool interface. It supports reading campaign analytics and, with write-scoped credentials, changing pages, media, entries, and webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A write-scoped Tokei API key allows campaign changes such as page updates, publishing, entry creation, media uploads, and webhook changes. <br>
Mitigation: Use a read-only key for monitoring and only provide a read+write key when the task intentionally changes campaign state. <br>
Risk: Page updates can replace entire prize, reward, or entry-method lists when incomplete arrays are submitted. <br>
Mitigation: Read the current page first, modify the full list, and submit the complete intended list in the update. <br>
Risk: Media fields reject local paths and most third-party URLs, and media upload tickets are quota-limited. <br>
Mitigation: Upload media with tokei-agent media:upload, use the returned public_url, and avoid speculative upload loops. <br>
Risk: Unpublishing blocks new signups but does not hide a page that already has a public URL. <br>
Mitigation: Tell users that unpublishing is not deletion or private hiding before using pages:unpublish. <br>
Risk: API responses can include personal data such as entrant email addresses, survey answers, and analytics. <br>
Mitigation: Treat CLI JSON output as sensitive and handle it according to the user's privacy and retention requirements. <br>


## Reference(s): <br>
- [Tokei agent documentation](https://tokei.io/agent) <br>
- [Tokei API reference](https://tokei.io/docs/api) <br>
- [Tokei OpenAPI specification](https://tokei.io/openapi.json) <br>
- [npm package](https://www.npmjs.com/package/tokei-agent) <br>
- [ClawHub skill page](https://clawhub.ai/gilesdawe/skills/tokei-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples; CLI and MCP executions return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Node 22+ runtime and a TOKEI_API_KEY for live Tokei API access.] <br>

## Skill Version(s): <br>
0.3.2 (source: package.json, server.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
