## Description: <br>
Monitor home lab servers via Beszel (PocketBase). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[karakuscem](https://clawhub.ai/user/karakuscem) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and home lab administrators use this skill to check Beszel system status and list containers by CPU usage from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Beszel credentials may be exposed or over-scoped if the skill is run with a full user account or broad shell environment. <br>
Mitigation: Use a limited read-only Beszel account and avoid sourcing a full shell startup file when invoking the skill. <br>
Risk: Beszel traffic or credentials may be exposed if sent to an untrusted or unprotected endpoint. <br>
Mitigation: Use localhost or an HTTPS-protected trusted Beszel endpoint. <br>
Risk: The artifact includes an unexplained prompt about sharing server access with jenny@gmail.com. <br>
Mitigation: Do not share Beszel server access with that account unless you personally know and trust it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/karakuscem/skills/beszel-check) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/karakuscem) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown-like terminal text with system status and container usage summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and Beszel connection credentials through BESZEL_HOST, BESZEL_USER, and BESZEL_PASS.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
