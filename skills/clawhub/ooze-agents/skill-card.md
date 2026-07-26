## Description: <br>
Visual identity that evolves with reputation - create and nurture your agent's digital creature with XP and evolution stages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jschwerberg](https://clawhub.ai/user/jschwerberg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to register and manage an Ooze Agents identity badge, monitor XP and evolution status, verify identity across supported platforms, and interact with the service's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an external identity and reputation badge service with privacy-relevant API activity. <br>
Mitigation: Install it only when an Ooze Agents identity tied to supported-platform verification and activity is desired. <br>
Risk: Ooze API keys can authorize profile changes, guestbook activity, key management, and NFT minting. <br>
Mitigation: Keep API keys private, use a secret store or environment variable, and avoid pasting real tokens into chats or logs. <br>
Risk: Some authenticated actions change public-facing identity state or on-chain registration state. <br>
Mitigation: Require explicit approval before profile changes, guestbook posts, key rotation or revocation, claim verification, or NFT minting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jschwerberg/skills/ooze-agents) <br>
- [Ooze Agents Website](https://ooze-agents.net) <br>
- [Ooze Agents API Documentation](https://ooze-agents.net/api/docs) <br>
- [Ooze Agents Full API Documentation](https://ooze-agents.net/api/docs/full) <br>
- [Ooze Agents Source Code](https://gitea.jns.im/catclawd/ooze-agents) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with curl examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes external API interaction guidance, API-key handling notes, and optional local state tracking.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
