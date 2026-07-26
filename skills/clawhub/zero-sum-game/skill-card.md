## Description: <br>
Helps agents diagnose whether a negotiation, market, policy, or strategy problem is truly zero-sum before choosing competitive or cooperative moves. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to test fixed-pie assumptions in strategy, negotiation, market-entry, policy, and competition questions. It guides the agent to name the contested resource, test whether the total value is fixed, audit zero-sum bias, and recommend either minimax/capture or cooperative surplus creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Important business, policy, financial, or negotiation recommendations may be incorrect or incomplete if accepted without review. <br>
Mitigation: Review high-stakes recommendations with qualified stakeholders before acting, especially where legal, financial, or policy consequences are material. <br>
Risk: The skill can misclassify a mixed or changing situation if the contested resource and time horizon are not stated clearly. <br>
Mitigation: Require the agent to name the resource, test fixity across innovation, cooperation, and time, and state the short-term and long-term diagnosis separately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/zero-sum-game) <br>
- [Primary sources](references/sources.md) <br>
- [Von Neumann and the Foundation of Zero-Sum Analysis](examples/von-neumann-rand-1944-1950.md) <br>
- [The Smoot-Hawley Tariff and the Fixed-Pie Fallacy in Trade](examples/smoot-hawley-tariff-1930.md) <br>
- [Where the AI Race Is Zero-Sum and Where It Isn't](examples/ai-competition-fixed-vs-growing-pie-2024-2026.md) <br>
- [Theory of Games and Economic Behavior](https://press.princeton.edu/books/paperback/9780691130613/theory-of-games-and-economic-behavior) <br>
- [The Strategy of Conflict](https://www.hup.harvard.edu/books/9780674840317) <br>
- [Equilibrium Points in N-Person Games](https://doi.org/10.1073/pnas.36.1.48) <br>
- [Zero-Sum Bias](https://doi.org/10.3389/fpsyg.2010.00191) <br>
- [Energy and AI](https://www.iea.org/reports/energy-and-ai) <br>
- [Artificial Intelligence Index Report 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown diagnosis with structured reasoning fields and a strategic recommendation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask step-by-step questions when the user lacks a concrete case; otherwise produces a zero-sum diagnosis and recommendation.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
