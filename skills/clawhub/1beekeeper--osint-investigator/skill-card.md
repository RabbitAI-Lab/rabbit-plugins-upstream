## Description: <br>
Open-source intelligence gathering with theHarvester, recon-ng, Maltego, and SpiderFoot. Domain recon, email harvesting, DNS mapping, and threat actor profiling from BlackArch tools on ARGUS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security analysts, investigators, and authorized red-team operators use this skill to gather OSINT on domains, emails, DNS records, SSL certificates, IP reputation, and related threat-intelligence context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reconnaissance workflows can collect sensitive emails, names, IPs, domains, and reports. <br>
Mitigation: Run investigations only with authorization and treat collected OSINT data as sensitive; review or delete saved reports after use. <br>
Risk: Broad or active modules can affect third-party systems or violate authorization boundaries. <br>
Mitigation: Keep scans passive by default and obtain written permission before using broad or active modules against external targets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1beekeeper/skills/osint-investigator) <br>
- [Publisher profile](https://clawhub.ai/user/1beekeeper) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces OSINT workflows and report-generation guidance; users choose targets and tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
