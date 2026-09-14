## Description:

Helps agents identify Ozon Russia blue-ocean categories by drilling from level-1 to level-3 categories, comparing sales and trend data against market baselines, and assessing saturation from hot-category and brand rankings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, ecommerce analysts, and agents use this skill to evaluate Ozon Russia category opportunities for new stores or new product lines. It guides category drill-down, trend comparison, saturation checks, and concise recommendations for 2 to 3 candidate niches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API token for market-research requests.

Mitigation: Provide the token only through the documented header or environment variables and confirm paid API calls before execution.

Risk: Large Ozon market-research result sets may be exported to local table files.

Mitigation: Run the skill in a workspace where storing Ozon market data locally is acceptable and review exported files before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-bluesea-hunter)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu login](https://www.iqinghu.com/workbench/login?type=1&urlCode=1788417429126)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown recommendations with JSON request examples and optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local table exports for larger result sets and should label figures with site, period, cycle, and sample size.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
