## Description: <br>
Scrapes Amazon product data from ASINs using browseract.com automation API and performs surgical competitive analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to collect Amazon product data for one or more ASINs and compare pricing, specifications, review signals, and competitive positioning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ASINs and related Amazon research activity are sent to BrowserAct under the user's account. <br>
Mitigation: Use the skill only for research activity that is appropriate to share with BrowserAct, and use a dedicated BrowserAct API key where possible. <br>
Risk: The BrowserAct API key may be loaded from an environment variable, .env file, or command-line argument. <br>
Mitigation: Protect the .env file, avoid sharing command histories or logs that include secrets, and rotate the key if it is exposed. <br>
Risk: The skill writes amazon_analysis.csv, amazon_analysis.md, and amazon_analysis.json in the selected output directory. <br>
Mitigation: Run it in an output directory where those filenames are expected, and review generated reports before sharing them. <br>


## Reference(s): <br>
- [BrowserAct](https://browseract.com) <br>
- [BrowserAct API Settings](https://www.browseract.com/reception/integrations) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, csv, json, shell commands, configuration] <br>
**Output Format:** [CLI status text plus local CSV, Markdown, and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes amazon_analysis.csv, amazon_analysis.md, and amazon_analysis.json to the selected output directory.] <br>

## Skill Version(s): <br>
0.1.6 (source: server release evidence; artifact documentation states 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
