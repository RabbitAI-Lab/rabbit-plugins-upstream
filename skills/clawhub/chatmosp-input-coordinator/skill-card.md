## Description: <br>
Entry skill of the ChatMOSP system that parses Chinese and English user requests, recognizes MSR, KMC, and parameter-query tasks, extracts simulation parameters, and coordinates companion ChatMOSP skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanyangye](https://clawhub.ai/user/sanyangye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers working with catalysis simulations use this skill to turn Chinese or English natural-language requests into confirmed MSR, KMC, or parameter-query workflows across the ChatMOSP companion skill set. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Companion skills dispatched by this coordinator may create files or run simulations. <br>
Mitigation: Review the companion ChatMOSP skills before installation and confirm generated parameters before allowing downstream execution. <br>
Risk: Broad trigger wording can match general metal-catalysis descriptions. <br>
Mitigation: Use explicit MSR, KMC, or parameter-query requests and rely on the skill's confirmation and clarification steps before routing work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanyangye/skills/chatmosp-input-coordinator) <br>
- [Publisher profile](https://clawhub.ai/user/sanyangye) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Markdown with extracted parameters, clarification prompts, confirmation text, and companion-skill routing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Coordinates companion ChatMOSP skills and does not by itself execute simulations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, created 2026-07-07T20:26:35Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
