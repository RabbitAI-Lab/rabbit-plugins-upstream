## Description: <br>
Skill Radar routes each user query to the most relevant available skills using declarative rules so agents can reduce prompt bloat and improve skill dispatch without ML infrastructure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ninetyhe-90](https://clawhub.ai/user/ninetyhe-90) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent platform teams use this skill to route multi-skill agent requests to the most relevant installed skills before assembling prompt context. It is useful when an agent has enough skills that loading all skill descriptions would add unnecessary context and reduce dispatch precision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence which other skills are loaded for many user queries. <br>
Mitigation: Review routing rules before deployment, keep fallback behavior available, and do not treat routing results as a security boundary. <br>
Risk: Self-routing mode may pass raw user text into a per-query command invocation. <br>
Mitigation: Integrate through safe subprocess argument passing or the Python API, and avoid shell interpolation of user-controlled text. <br>
Risk: The optional HTTP server can expose routing behavior if bound outside a trusted local environment. <br>
Mitigation: Bind the server only to trusted local use or place it behind appropriate network controls. <br>
Risk: Skills without routing declarations are invisible to the router until fallback behavior runs. <br>
Mitigation: Generate and review routing.yaml files for installed skills that should participate in routing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ninetyhe-90/skills/skill-radar) <br>
- [Routing Schema Specification](references/routing-schema.md) <br>
- [Scoring Theory](references/scoring-theory.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with shell commands, YAML routing configuration examples, Python code snippets, and JSON routing results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routing output includes matched skills, scores, and exclusions for auditability.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and release changelog; artifact frontmatter and pyproject.toml report 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
