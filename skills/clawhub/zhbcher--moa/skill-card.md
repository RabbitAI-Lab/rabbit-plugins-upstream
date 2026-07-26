## Description: <br>
Mixture-of-Agents: run multiple reference models in parallel, then aggregate with current agent for deeper analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhbcher](https://clawhub.ai/user/zhbcher) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to get parallel advisory responses from configured reference LLM providers and synthesize them through the current agent. It supports general analysis, coding review, architecture review, writing feedback, status checks, diagnostics, and optional persistent MoA mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User prompts are sent to configured external LLM providers for parallel advice. <br>
Mitigation: Use the skill only for prompts that are appropriate to share with those providers, configure only intended providers, and review each provider's data handling terms. <br>
Risk: Persistent mode can route later messages through MoA without an explicit /moa command. <br>
Mitigation: Avoid persistent mode for sensitive chats, check state with /moa status, and turn it off with /moa off when the MoA workflow is no longer intended. <br>
Risk: /moa doctor produces local diagnostic information about provider configuration and reachability. <br>
Mitigation: Treat diagnostic output as local operational information and avoid sharing it in public or untrusted channels. <br>


## Reference(s): <br>
- [Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692) <br>
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown responses with embedded reference-model summaries, status text, diagnostic reports, and inline shell or JSON configuration examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reference outputs include provider/model identifiers, latency, rank, quality class, quality-gate statistics, token usage, and estimated cost when available.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
