## Description: <br>
Research HS300 index constituents for stock analysis and portfolio construction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research analysts use this skill to collect multi-source market data, score CSI 300 constituents with quantitative factors, and generate HS300 research reports for stock analysis and portfolio construction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release exposes service credentials. <br>
Mitigation: Remove packaged credentials, rotate exposed secrets, and require users to configure their own credentials before running the skill. <br>
Risk: The skill can produce investment-style guidance from misleading or simulated data paths. <br>
Mitigation: Validate data provenance, clearly watermark simulated inputs, and treat generated reports as research support rather than trading advice. <br>
Risk: External data queries and unpinned dependencies may broaden operational risk. <br>
Mitigation: Scope third-party queries to the intended HS300 workflow and pin dependencies before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/hs300-research-v5) <br>
- [README](artifact/README.md) <br>
- [Data sources](artifact/DATA_SOURCES.md) <br>
- [Tushare Pro](https://tushare.pro) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, Excel workbooks, CSV factor data, and terminal text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses external financial data services and may require user-provided API credentials.] <br>

## Skill Version(s): <br>
5.2.2 (source: server release metadata; artifact frontmatter lists 5.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
