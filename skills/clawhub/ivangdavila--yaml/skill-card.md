## Description: <br>
YAML helps agents write, debug, validate, edit, and secure YAML files across parsers, schemas, and common toolchains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to produce, inspect, patch, and validate YAML for configuration files, CI pipelines, Kubernetes and Helm manifests, Compose files, OpenAPI documents, and similar YAML-based systems. It is especially useful when parser differences, implicit type coercion, indentation, block scalars, anchors, schemas, or unsafe loaders could change behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill maintains local notes about YAML files, parser/tooling facts, repo style, workflow errors, and preferences, and those local notes may reveal sensitive project metadata. <br>
Mitigation: Install only where that local persistence is acceptable; review the configured Clawic paths and avoid recording sensitive project details. <br>
Risk: YAML files often contain credentials or PEM blocks that could be copied into local memory if handled carelessly. <br>
Mitigation: Store secret pointers such as environment-variable, keychain, 1Password, sops, or file references instead of secret values, matching the skill's documented behavior. <br>
Risk: YAML parser differences and implicit type coercion can produce valid YAML with incorrect runtime types. <br>
Mitigation: Validate generated or edited YAML with the target consumer's parser and schema checks before deployment. <br>


## Reference(s): <br>
- [ClawHub YAML Skill Page](https://clawhub.ai/ivangdavila/skills/yaml) <br>
- [Clawic YAML Skill Page](https://clawic.com/skills/yaml) <br>
- [YAML Security Notes](artifact/security.md) <br>
- [YAML Parser Matrix](artifact/parsers.md) <br>
- [YAML Schema and Linting Notes](artifact/schemas.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose with YAML snippets, patches, validation commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update local Clawic note files for YAML preferences, project facts, and validation outcomes when configured.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
