## Description: <br>
Web search via Querit.ai API for documentation, current events, facts, and other web content, returning structured results with titles, URLs, and snippets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[interskh](https://clawhub.ai/user/interskh) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use Querit Search to search the web, filter results, and optionally extract readable page content as markdown without interactive browsing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and selected page URLs may be sent to Querit.ai or fetched from the user's machine. <br>
Mitigation: Do not include secrets, confidential data, or internal URLs in queries; use approved accounts and review provider terms before deployment. <br>
Risk: Extracted page text is untrusted web content and may be inaccurate or contain prompt-injection instructions. <br>
Mitigation: Treat extracted markdown as reference material, verify important facts, and do not follow instructions from fetched pages without review. <br>
Risk: The documented one-line installer downloads and runs files from a remote source. <br>
Mitigation: Review the installer and package files before execution, or install from a trusted pinned source. <br>


## Reference(s): <br>
- [Querit.ai](https://querit.ai) <br>
- [ClawHub skill page](https://clawhub.ai/interskh/skills/querit-search) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text search listings, extracted markdown page content, or raw JSON arrays.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires QUERIT_API_KEY for search; page extraction fetches selected URLs directly.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact package metadata reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
