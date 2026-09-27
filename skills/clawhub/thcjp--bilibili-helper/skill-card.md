## Description: <br>
Bilibili Helper helps Bilibili content creators draft Chinese video titles, descriptions, tags, spoken scripts, and publishing strategy suggestions from a supplied topic or content brief. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and content teams use this skill to prepare Bilibili upload copy, including title options, structured descriptions, tag recommendations, spoken scripts, and lightweight channel operations guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the skill asks for broad command, file, API, and credential-related capabilities that are not clearly needed or scoped. <br>
Mitigation: Install and run it as a prompt-only writing helper unless the publisher narrows the scope; do not grant shell, write, API credential, callback, or broad file access by default. <br>
Risk: Generated titles, tags, scripts, and publishing advice can be inaccurate, stale, or misaligned with current Bilibili rules and audience behavior. <br>
Mitigation: Have a human creator review outputs against current platform policies, topic facts, and channel context before publishing. <br>
Risk: The artifact describes optional command-driven use through a shell script, but the release package only provides SKILL.md evidence here. <br>
Mitigation: Treat command examples as unverified workflow examples unless the corresponding script is supplied and reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bilibili-helper) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text with optional shell command snippets and JSON-style response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primarily Chinese-language generated content for manual review and use in Bilibili publishing workflows.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
