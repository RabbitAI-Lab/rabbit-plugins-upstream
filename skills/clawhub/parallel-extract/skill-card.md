## Description: <br>
URL content extraction via Parallel API. Extracts clean markdown from webpages, articles, PDFs, and JS-heavy sites. Use for reading specific URLs with LLM-ready output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[normallygaussian](https://clawhub.ai/user/normallygaussian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to extract clean, LLM-ready content from specific URLs, including webpages, articles, PDFs, and JavaScript-heavy sites. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided URLs and extracted content are processed through Parallel's authenticated CLI, which may expose sensitive or confidential material to an external service. <br>
Mitigation: Avoid sending private, internal, token-bearing, authenticated, or confidential URLs unless that handling is intended. <br>
Risk: Temporary extraction files may contain sensitive page content. <br>
Mitigation: Remove temporary extraction files after use when they contain sensitive material. <br>
Risk: The skill depends on parallel-cli being installed and authenticated. <br>
Mitigation: Verify parallel-cli is installed and authenticated before use; stop and consult the Parallel CLI integration documentation if installation or authentication fails. <br>


## Reference(s): <br>
- [Parallel Homepage](https://parallel.ai) <br>
- [Parallel API Docs](https://docs.parallel.ai) <br>
- [Parallel Extract API Reference](https://docs.parallel.ai/api-reference/extract) <br>
- [Parallel CLI Integration Docs](https://docs.parallel.ai/integrations/cli) <br>
- [ClawHub Skill Page](https://clawhub.ai/normallygaussian/skills/parallel-extract) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON extraction output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an installed and authenticated parallel-cli; extracted URL content may include excerpts, full content, titles, URLs, and publish dates.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
