## Description: <br>
Calibre catalog lookup, viewing, and delegated one-book analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect a Calibre catalog, retrieve book details, and coordinate one-book analysis through a constrained subagent workflow. It is intended for existing Calibre Content server environments where lookup and analysis comments are part of the user's library workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Analysis completion can write generated analysis into a book's Calibre comments. <br>
Mitigation: Review the target book and generated analysis before routine use, and use a dedicated low-privilege Calibre account where possible. <br>
Risk: Credential handling has avoidable leakage risk when connecting to the Calibre Content server. <br>
Mitigation: Keep CALIBRE_* environment files scoped to the runtime, prefer CALIBRE_PASSWORD over inline passwords, and review password-redaction behavior before deployment. <br>
Risk: Low extracted text or comic-centric titles can produce poor or inappropriate text analysis. <br>
Mitigation: Follow the built-in low-text confirmation step and exclude manga or comic-centric books from the text analysis pipeline. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/calibre-catalog-read) <br>
- [README](README.md) <br>
- [Subagent Analysis Prompt](references/subagent-analysis.prompt.md) <br>
- [Subagent Analysis Schema](references/subagent-analysis.schema.json) <br>
- [Subagent Input Schema](references/subagent-input.schema.json) <br>
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON schema contracts; delegated book analysis returns schema-valid JSON and can be rendered into Calibre comments.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node, uv, calibredb, ebook-convert, and CALIBRE_PASSWORD; optional CALIBRE_USERNAME may be used for authenticated Calibre Content server access.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
