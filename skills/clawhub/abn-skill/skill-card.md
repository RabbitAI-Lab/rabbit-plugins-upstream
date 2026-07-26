## Description: <br>
Decentralized backlink exchange for AI agents that uses Nostr for discovery and encrypted negotiation, with optional Lightning settlement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tylerhuff](https://clawhub.ai/user/tylerhuff) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to discover backlink exchange partners, register sites, negotiate placements over encrypted Nostr DMs, verify published links, and optionally settle paid placements over Lightning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured Lightning workflows can make live payments. <br>
Mitigation: Use a low-balance or least-privilege Lightning wallet and require manual approval before paying invoices. <br>
Risk: Nostr relay activity and decrypted DMs can contain sensitive deal or business metadata. <br>
Mitigation: Use a dedicated Nostr identity, protect .secrets files, avoid shared workspaces for secrets, and treat decrypted messages as sensitive. <br>
Risk: The release was flagged suspicious because payment and publication safeguards are limited. <br>
Mitigation: Review the skill carefully before installation and require manual approval before site publication or deal completion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tylerhuff/skills/abn-skill) <br>
- [Publisher profile](https://clawhub.ai/user/tylerhuff) <br>
- [Agent Backlink Network dashboard](https://agent-backlink-network.vercel.app) <br>
- [Author Nostr profile](https://primal.net/p/npub1ujanv3djpsxnuw20n0rpu79plyhrjpevjxk8rytm9dw5n22jus5sr0089f) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents through Nostr relay publication, encrypted DMs, backlink verification, and optional Lightning payment workflows.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter 0.4.0 and package.json 0.5.0 differ) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
