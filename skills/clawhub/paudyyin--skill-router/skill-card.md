## Description: <br>
Always-on入口 - 所有消息先调用此skill，由它分析意图、路由到最优技能或组合包。支持显式调用(@skill/Bundle)和自然语言路由。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill as an always-on routing entry point to classify user intent and delegate work to a selected skill or bundle. It supports explicit @skill and /bundle commands as well as natural-language routing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a broad always-on router and can become the default gatekeeper for user messages. <br>
Mitigation: Review the routing behavior before deployment and require human confirmation for sensitive or ambiguous routing decisions. <br>
Risk: The skill runs a referenced local router_engine.py script that is not included in the package. <br>
Mitigation: Install only after verifying the referenced router_engine.py source, path, and trust boundary in the target environment. <br>
Risk: The skill may dispatch other active or archived skills with limited containment when routing succeeds. <br>
Mitigation: Limit the callable skill set to approved skills and review routed bundle chains before enabling unattended use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/skill-router) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON routing examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes agent work to another skill or bundle; it does not directly perform the delegated task.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
