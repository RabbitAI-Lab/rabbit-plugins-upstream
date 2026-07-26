## Description: <br>
MiniMax lets an agent operate MiniMax through an OOMOL-connected account for model discovery, token estimation, and non-streaming response creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect MiniMax connector schemas, list or retrieve OpenAI-compatible MiniMax model metadata, estimate input tokens, and create non-streaming MiniMax responses through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on OOMOL as the credential-handling connector for MiniMax. <br>
Mitigation: Install only if that connector model is acceptable, and avoid handling raw MiniMax credentials outside the OOMOL connection flow. <br>
Risk: The first-time setup path includes remote oo CLI installer commands. <br>
Mitigation: Treat the installer like any third-party installer and review it before running it; use setup commands only when oo is missing or authentication fails. <br>
Risk: The create_response action changes MiniMax state by creating a non-streaming response. <br>
Mitigation: Fetch the live connector schema, review the exact JSON payload and expected effect, and get user confirmation before running the write action. <br>


## Reference(s): <br>
- [MiniMax homepage](https://www.minimax.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [MiniMax ClawHub listing](https://clawhub.ai/oomol/skills/oo-minimax) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo connector schemas and JSON payloads; create_response is a write action.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
