## Description: <br>
Helps agents analyze negotiations, conflicts, and platform dynamics to identify whether mutual gains are possible and design cooperation mechanisms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill when a negotiation, conflict, market, platform, contract, or institution feels win-lose and needs a structured test for latent cooperative value. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may steer agents toward a non-zero-sum framing even when a situation is genuinely fixed-pool, one-shot, values-based, or power-asymmetric. <br>
Mitigation: Apply the documented fit checks and stop rule before using the framework; redirect to a more appropriate strategy when cooperation cannot create net value. <br>
Risk: Business and market examples may be illustrative rather than verified current market facts. <br>
Mitigation: Treat examples as guidance and verify time-sensitive claims against current authoritative sources before using them in decisions. <br>


## Reference(s): <br>
- [Non-Zero-Sum skill page](https://clawhub.ai/deciqai/skills/non-zero-sum) <br>
- [Sources - non-zero-sum](references/sources.md) <br>
- [Axelrod's Computer Tournament example](examples/axelrods-computer-tournament-1980.md) <br>
- [AI Ecosystem Value Creation example](examples/ai-ecosystem-value-creation-2024-2026.md) <br>
- [The Evolution of Cooperation](https://www.basicbooks.com/titles/robert-axelrod/the-evolution-of-cooperation/9780465021215/) <br>
- [Effective Choice in the Prisoner's Dilemma](https://doi.org/10.1177/002200278002400101) <br>
- [Evolutionary Games and Spatial Chaos](https://doi.org/10.1038/359826a0) <br>
- [Microsoft and OpenAI extend partnership](https://blogs.microsoft.com/blog/2023/01/23/microsoftandopenaiextendpartnership/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis with tables and structured sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask step-by-step coaching questions and wait for user input when no concrete case is provided.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
