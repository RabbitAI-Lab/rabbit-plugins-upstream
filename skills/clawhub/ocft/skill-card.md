## Description: <br>
P2P file transfer between AI agents via message channels, with chunked transfer, IPFS fallback for large files, and trusted peer management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stormixus](https://clawhub.ai/user/stormixus) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to transfer files between trusted AI agents over text-based channels such as chat systems, with support for chunking, resume, integrity checks, and optional IPFS fallback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Node secrets and IPFS keys could expose trusted transfer relationships or storage access if shared outside intended peers. <br>
Mitigation: Keep secrets and provider keys private, rotate them if exposed, and use trust expiration for peer relationships. <br>
Risk: Auto-accept can receive files without manual review when a peer secret is trusted. <br>
Mitigation: Enable auto-accept only for trusted peers, set appropriate TTLs, and restrict the download directory. <br>
Risk: Received files may be unsafe if opened or executed automatically. <br>
Mitigation: Do not automatically execute received files; inspect or scan files before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stormixus/skills/ocft) <br>
- [Project homepage](https://github.com/stormixus/ocft) <br>
- [npm package](https://www.npmjs.com/package/ocft) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, CLI examples, TypeScript snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational guidance for using the ocft CLI and API; does not itself transfer files without the user running the documented commands.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
