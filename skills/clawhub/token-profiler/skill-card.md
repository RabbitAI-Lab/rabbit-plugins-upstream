## Description: <br>
Fetch a free structured token profile for Solana or Base. Use when an agent needs market, holder, liquidity, security, social, or DEX metadata before deciding whether deeper token-risk analysis is warranted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vswarm-ai](https://clawhub.ai/user/vswarm-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external agents use Token Profiler to fetch structured Solana or Base token metadata before deciding whether deeper token-risk analysis is warranted. It supports discovery and screening, not final safety or trading decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Token addresses and selected chains are sent to VerdictSwarm's API and may be associated with request metadata such as client IP. <br>
Mitigation: Avoid submitting confidential internal identifiers when that disclosure is a concern. <br>
Risk: A profile can contain missing or null fields and is not a complete safety verdict. <br>
Mitigation: Disclose unavailable data and use a dedicated verdict workflow for pre-trade decisions. <br>


## Reference(s): <br>
- [ClawHub Token Profiler Skill](https://clawhub.ai/vswarm-ai/skills/token-profiler) <br>
- [VerdictSwarm](https://www.vswarm.io) <br>
- [VerdictSwarm API Documentation](https://www.vswarm.io/docs/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and structured JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl for command examples; the public endpoint is unauthenticated and rate limited.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
