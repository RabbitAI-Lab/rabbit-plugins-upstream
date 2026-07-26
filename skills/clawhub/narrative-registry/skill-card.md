## Description: <br>
Helps agents record and query a brand's versioned narrative canon, message hierarchy, voice and naming rules, and canon revision decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing strategy and brand teams use this skill through compatible agent hosts to maintain canonical brand narrative records. It helps downstream content builders receive exact canon/version pointers instead of redefining positioning, claims, voice, or naming rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authorized writes can change the brand narrative canon and generated views. <br>
Mitigation: Require explicit user authorization, review complete canon proposals, and verify current revision and claim pointers before accepting changes. <br>
Risk: Using the skill without the required host capabilities can create handoffs that appear canonical when they are only proposals. <br>
Mitigation: When the host runtime, schema, or catalog is unavailable, leave a bounded proposal and do not claim canonical narrative truth. <br>


## Reference(s): <br>
- [Narrative Registry on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/narrative-registry) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline commands and structured handoff notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit authorization before canonical writes; leaves bounded proposals when the required host runtime is unavailable.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
