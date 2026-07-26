## Description: <br>
Structured memory system for AI agents. Context death resilience (checkpoint/recover), structured storage, Obsidian-compatible markdown, and local semantic search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[azrijamil](https://clawhub.ai/user/azrijamil) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to maintain structured local memory across sessions, including checkpoints, handoffs, typed notes, vault migration, and search over Obsidian-compatible Markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a global npm package and an optional GitHub-hosted search dependency. <br>
Mitigation: Install only when the Foresigxt npm package and optional qmd package are trusted for the target environment. <br>
Risk: Local memory vaults can accumulate sensitive project, personal, or credential-adjacent information. <br>
Mitigation: Use workspace-specific vaults for sensitive projects, avoid storing secrets or regulated personal data, and keep vault and .env files out of public repositories or broad sync folders. <br>
Risk: Migration commands can modify existing Markdown vault structures. <br>
Mitigation: Run migrations with --dry-run first and use backup mode before applying changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/azrijamil/skills/fsxmemory) <br>
- [Foresigxt CLI Memory npm Package](https://www.npmjs.com/package/@foresigxt/foresigxt-cli-memory) <br>
- [Foresigxt CLI Memory Repository](https://github.com/Foresigxt/foresigxt-cli-memory) <br>
- [qmd Search Dependency](https://github.com/tobi/qmd) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured memory templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Obsidian-compatible Markdown memory vault content; semantic search requires qmd.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.3.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
