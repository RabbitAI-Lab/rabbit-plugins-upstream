## Description: <br>
Halo guides agents through HALO V5.0 A-share fundamental analysis by fetching market and qualitative data, generating a locked-data report skeleton, and filling analysis sections without inventing missing data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lululu811](https://clawhub.ai/user/lululu811) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use Halo to run structured A-share stock analysis from a stock code or company name and produce a Markdown report with data-backed scoring and investment commentary. Generated investment analysis should be reviewed as informational rather than treated as a trading instruction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated stock analysis or investment commentary may be mistaken for a trading instruction. <br>
Mitigation: Review the report as informational analysis and apply independent financial judgment before acting. <br>
Risk: The workflow fetches market data and writes local reports, so stale, missing, or failed data retrieval can affect conclusions. <br>
Mitigation: Invoke `/halo <code or name>` intentionally, check missing-data markers, and review generated files before relying on the report. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/lululu811/halo-skill) <br>
- [a-stock-data bridge reference](https://github.com/simonlin1212/a-stock-data) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and structured analysis guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local data JSON, report skeletons, and final Markdown reports when paired with the referenced scripts; users should review generated investment analysis before relying on it.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
