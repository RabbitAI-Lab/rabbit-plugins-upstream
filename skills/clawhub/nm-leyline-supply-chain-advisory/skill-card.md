## Description: <br>
Audits dependency supply chains for bad versions, lockfile drift, and artifact integrity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security engineers use this skill to audit Python dependency supply chains, check lockfiles and package versions against known-bad indicators, and guide incident response for suspected package compromise. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest broad local searches or environment snapshots during incident response, which can expose sensitive project paths or secrets. <br>
Mitigation: Run suggested commands only for a real supply-chain investigation, scope searches to relevant project directories where possible, and treat captured environment output as sensitive. <br>
Risk: Manual supply-chain checks can miss zero-day compromises or advisories that have not reached vulnerability databases. <br>
Mitigation: Pair the guidance with lockfile hash verification, version exclusions, CI scanning, and human review of current advisories before making remediation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-supply-chain-advisory) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with checklists, command examples, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local filesystem searches and environment snapshots during supply-chain incident response.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
