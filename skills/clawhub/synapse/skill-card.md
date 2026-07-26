## Description: <br>
Agent-to-agent P2P file sharing with semantic search using BitTorrent and vector embeddings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pendzoncymisio](https://clawhub.ai/user/pendzoncymisio) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use Synapse to share files or memory shards over a P2P network, discover shared content through semantic search, and download matching content by magnet link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a P2P file-sharing node that can expose local files and semantic metadata through trackers. <br>
Mitigation: Use it only for intended P2P sharing, avoid confidential or regulated files, and prefer trusted HTTPS trackers. <br>
Risk: The background seeder has weak local controls and may continue sharing after initial use. <br>
Mitigation: Monitor the seeder status, stop the daemon when finished, and restrict or patch local seeder access before deployment. <br>
Risk: Downloaded shards or dependencies may introduce untrusted content into an agent workflow. <br>
Mitigation: Inspect the uv installer and dependencies, scan downloaded shards, and verify content before assimilating it into an agent memory store. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/pendzoncymisio/skills/synapse) <br>
- [Synapse README](artifact/README.md) <br>
- [Synapse Installation and Usage](artifact/SKILL.md) <br>
- [SynapseTracker Server Implementation](https://github.com/Pendzoncymisio/SynapseTracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, configuration] <br>
**Output Format:** [CLI text output, magnet links, downloaded files, and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May start or control a background seeder and perform P2P uploads or downloads.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
