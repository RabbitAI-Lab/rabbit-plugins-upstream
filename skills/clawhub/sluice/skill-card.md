## Description: <br>
An outbound egress guard for agents that scans messages for leaked secrets and private identifiers before they are sent, then blocks or redacts findings in place. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workloftai](https://clawhub.ai/user/workloftai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use sluice as a pre-send guard for outbound email, social drafts, chat replies, and public-site writes. It helps catch API keys, tokens, private keys, private paths, and private IPs before content leaves the local environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scanned outbound drafts and files may contain sensitive content. <br>
Mitigation: Pass only drafts or files intended for inspection, and handle scan output as sensitive even though previews avoid echoing full secrets. <br>
Risk: The benchmark script scans hardcoded local publication and draft paths. <br>
Mitigation: Avoid running bench.py unless you understand and intend that local-path scanning behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workloftai/skills/sluice) <br>
- [Workloft Labs](https://workloft.ai/labs) <br>
- [Workloft support](https://workloft.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text redactions, stderr findings, or JSON finding reports from a Python CLI.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scan mode exits non-zero at or above the configured severity threshold; redact mode writes cleaned content to stdout.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
