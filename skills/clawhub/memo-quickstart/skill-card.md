## Description: <br>
Memo Quickstart helps agents set up a zero-dependency local memory layer with three-tier storage, weighted TF-IDF retrieval, WAL-style persistence steps, relationship links, and migration commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to initialize and operate a local memory layer for preferences, decisions, facts, lessons, and context, especially in offline or privacy-sensitive workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores conversation-derived preferences, decisions, deadlines, corrections, and other context on local disk. <br>
Mitigation: Avoid storing secrets, credentials, health, financial, or other sensitive personal data; review where files are written and how to delete or export them before use. <br>
Risk: Optional callback or GitHub Gist sync features can share memory data outside the local machine. <br>
Mitigation: Confirm the destination before enabling callbacks or sync, and keep network sharing disabled for local-only use. <br>
Risk: Stored memory can become stale, inaccurate, or too large for effective local retrieval. <br>
Mitigation: Use the documented archive, cleanup, deduplication, and export commands, and review stored memory before relying on it. <br>


## Reference(s): <br>
- [Memo Quickstart ClawHub Page](https://clawhub.ai/thcjp/skills/memo-quickstart) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and bash command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local memory files when the agent follows the described CLI workflow.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
