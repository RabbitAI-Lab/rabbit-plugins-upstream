## Description: <br>
Generate WHO child growth charts (height, weight, BMI) with percentile curves. Downloads official WHO reference data on demand. Use when users ask about child growth tracking, percentiles, or want growth charts for their kids. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Parents, caregivers, and developers can use this skill to generate WHO-based height, weight, and BMI growth charts from child measurement data. It is useful for visualizing percentile curves and local measurement trends, not for replacing professional medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child measurement JSON files and generated charts can contain private health-related data. <br>
Mitigation: Store measurement files and chart outputs locally, restrict sharing, and delete the output/cache directory when no longer needed. <br>
Risk: The skill downloads WHO reference files from cdn.who.int and depends on Python charting libraries. <br>
Mitigation: Install only in environments that allow these dependencies and outbound WHO downloads, and review generated charts before relying on them. <br>


## Reference(s): <br>
- [ClawHub WHO Growth Charts skill page](https://clawhub.ai/odrobnik/skills/who-growth-charts) <br>
- [WHO child growth standards data](https://cdn.who.int/media/docs/default-source/child-growth/child-growth-standards/indicators) <br>
- [WHO growth reference data for ages 5-19](https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated PNG chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 with pandas, matplotlib, scipy, and openpyxl; downloads WHO reference files on demand and stores generated charts plus cache files locally.] <br>

## Skill Version(s): <br>
1.2.3 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
