## Description: <br>
Scan a public GitHub repository, folder, or file containing an AI agent skill with Longxia's static pre-install security scanner. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[john-dong-ai](https://clawhub.ai/user/john-dong-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and reviewers use this skill to scan public GitHub-hosted agent skills before installation or manual review. It helps inspect risky instructions, scripts, permissions, credential access, network behavior, package installation, and supply-chain signals without executing the target repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the user-provided public GitHub URL to Longxia's remote scanning service. <br>
Mitigation: Use only public GitHub URLs and do not provide private repositories, credential-bearing URLs, internal links, or sensitive query parameters. <br>
Risk: A clean static scan result is advisory and does not prove that a skill is safe. <br>
Mitigation: Manually review the scanned content, requested capabilities, and any generated report before installation or deployment. <br>


## Reference(s): <br>
- [Longxia homepage](https://longxia.cool) <br>
- [ClawHub skill page](https://clawhub.ai/john-dong-ai/skills/longxia-scan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary with command guidance, scan findings, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include verdict, risk score, finding counts, affected files, remediation notes, report expiry, and remaining anonymous scans.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
