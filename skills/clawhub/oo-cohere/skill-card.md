## Description: <br>
Operates Cohere through an OOMOL-connected account using the oo CLI for chat, embeddings, and document reranking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to send Cohere chat, embedding, and reranking requests through an OOMOL-connected account without handling raw Cohere credentials directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and documents sent to chat, embed, or rerank are transmitted to external services. <br>
Mitigation: Review user data before execution and avoid sending sensitive content unless the connected Cohere and OOMOL accounts are approved for that data. <br>
Risk: First-time setup may require installing or authenticating the oo CLI. <br>
Mitigation: Review the oo CLI installer before running setup and only install it when the user intends to use OOMOL with a connected Cohere account. <br>
Risk: Connector actions depend on the current live schema and account connection state. <br>
Mitigation: Inspect the connector schema before constructing payloads and use first-time setup steps only after matching authentication, connection, or billing errors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cohere) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Cohere homepage](https://cohere.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples; connector responses are JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
