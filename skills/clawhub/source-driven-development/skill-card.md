## Description: <br>
Drive development from authoritative source documentation and specifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to make framework-specific code decisions from official documentation, detect project stack versions, implement current patterns, and cite sources for non-obvious choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may read normal project dependency files and browse official documentation while following the workflow. <br>
Mitigation: Confirm this access pattern is acceptable before installation and keep documentation lookups scoped to authoritative sources needed for the task. <br>
Risk: Non-Chinese users may find the current skill text harder to audit or operate because it does not provide an explicit language fallback. <br>
Mitigation: Have a fluent reviewer validate the skill text or provide an explicit language fallback before relying on it in production. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/source-driven-development) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with code and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes source citations for framework-specific decisions and explicit notes when a pattern is unverifiable.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
