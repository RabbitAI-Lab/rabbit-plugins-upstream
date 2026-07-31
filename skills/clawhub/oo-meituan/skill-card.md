## Description: <br>
Meituan supports agent-driven Meituan search and data-reading tasks through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Meituan Travel for flights, trains, hotels, attractions, itineraries, local transportation, and related travel information through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a remote CLI installer and a persistent OOMOL-connected Meituan account. <br>
Mitigation: Before installation or use, confirm the publisher is trusted and that connecting a Meituan account through OOMOL is acceptable. <br>
Risk: Future Meituan actions could be tagged as write or destructive even though current behavior is limited to read-style travel queries. <br>
Mitigation: Require explicit user confirmation for any tagged write or destructive action before execution. <br>


## Reference(s): <br>
- [Meituan Skill Page](https://clawhub.ai/oomol/skills/oo-meituan) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Meituan Homepage](https://www.meituan.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Meituan travel-query requests may require a caller timeout longer than 120 seconds.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
