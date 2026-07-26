## Description: <br>
Guides agents in analyzing capital, resource-allocation, customer, deal, employee-performance, risk-model, and venture-return decisions where power-law distributions may make averages or Gaussian assumptions misleading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, operators, and decision-makers use this skill to test whether portfolio, revenue, performance, or risk outcomes are power-law distributed and to redesign allocation, risk sizing, and monitoring around upper-tail concentration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial and business examples may be outdated, incomplete, or unsuitable as sole decision inputs. <br>
Mitigation: Verify current market claims independently and treat outputs as decision-support material rather than a substitute for domain-specific risk review. <br>
Risk: Users may force power-law framing onto data that is actually Gaussian or otherwise not tail-dominated. <br>
Mitigation: Apply the skill's empirical stop rule: check top-N share, mean-to-median ratio, tail shape, and log-log fit before redesigning allocation or risk models. <br>


## Reference(s): <br>
- [Sources - power-law-distribution](references/sources.md) <br>
- [Pareto 1896, Mandelbrot 1963, and VC Return Data](examples/pareto-1896-mandelbrot-1963-and-vc-return-data.md) <br>
- [AI and Venture Returns Concentration (2023-2026)](examples/ai-venture-returns-concentration-2023-2026.md) <br>
- [deciqAI Power-Law Distribution Skill Page](https://www.deciqai.com/c/power-law-distribution) <br>
- [Power-Law Distribution Machine-Readable Metadata](https://www.deciqai.com/s/power-law-distribution.json) <br>
- [NVIDIA Investor Relations](https://investor.nvidia.com/) <br>
- [U.S. Bureau of Industry and Security](https://www.bis.gov/) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown analysis with structured decision checkpoints] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May pause for user input during novice coaching before completing the analysis.] <br>

## Skill Version(s): <br>
1.0.4 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
