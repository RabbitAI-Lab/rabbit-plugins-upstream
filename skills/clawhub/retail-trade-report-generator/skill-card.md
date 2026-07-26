## Description: <br>
Generates a consolidated weekly retail trade report from local sales Excel files, including regional and channel ADA totals, week-over-week comparisons, and formatted Excel output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuminmin](https://clawhub.ai/user/wuminmin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Retail sales operations analysts and business users use this skill to turn weekly retail sales spreadsheets into a consolidated Excel workbook for reviewing regional, channel, product, ADA, and week-over-week performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Store alias gaps or fuzzy matching can assign sales to the wrong region or to Others. <br>
Mitigation: Review store_mapping.csv aliases and validate regional totals in the generated workbook before business use. <br>
Risk: The skill reads local retail sales spreadsheets and writes a generated Excel report. <br>
Mitigation: Run it only on intended input files and review the output before sharing or relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wuminmin/skills/retail-trade-report-generator) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Store mapping CSV](artifact/references/store_mapping.csv) <br>


## Skill Output: <br>
**Output Type(s):** [code, configuration, guidance, files] <br>
**Output Format:** [Python usage guidance and a generated Excel workbook (.xlsx)] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads 12 user-provided weekly sales Excel files plus a store mapping CSV and writes one formatted report workbook.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
