## Description: <br>
YAML helps agents write, debug, validate, and safely edit YAML across parsers, schemas, CLIs, CI systems, Kubernetes, and other YAML-consuming tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to generate, repair, review, and validate YAML files while avoiding parser-specific type coercion, indentation, multiline, anchor, schema, and secret-handling mistakes. It is also suited for maintaining YAML-related project notes and preferences when local Clawic memory is intentionally used. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read and change long-term local YAML, project, and device memory under ~/Clawic/data. <br>
Mitigation: Install only when that local memory behavior is desired, review those files periodically, and ask the agent to confirm before persistent writes or memory cleanup. <br>
Risk: YAML examples and memory files can accidentally capture secrets, especially PEM blocks, Kubernetes Secret values, tokens, or connection strings. <br>
Mitigation: Keep secret values out of ~/Clawic/data and YAML files; store only pointers such as environment variable, keychain, sops, vault, or file references. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/yaml) <br>
- [Skill homepage](https://clawic.com/skills/yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML snippets, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local YAML memory under ~/Clawic/data when durable project facts, preferences, or safety decisions are established.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
