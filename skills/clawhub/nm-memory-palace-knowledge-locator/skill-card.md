## Description: <br>
Searches and navigates stored knowledge in memory palaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to locate concepts, decisions, patterns, and related information across memory-palace knowledge stores. It helps agents choose spatial, semantic, sensory, associative, or temporal retrieval strategies and surface relevant review knowledge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers can cause the skill to activate during ordinary search or recall requests. <br>
Mitigation: Confirm the task actually involves memory-palace retrieval before following the skill's search workflow. <br>
Risk: The related full plugin may maintain local indices and access metadata for palace content. <br>
Mitigation: Review local index storage and access metadata handling before enabling the broader memory-palace plugin workflow. <br>
Risk: Example commands depend on local palace-management scripts and related memory-palace configuration. <br>
Mitigation: Verify the required local scripts and companion skills are installed before running command examples. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-memory-palace-knowledge-locator) <br>
- [Memory Palace plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace) <br>
- [Index Structure](modules/index-structure.md) <br>
- [Search Strategies](modules/search-strategies.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference related memory-palace skills and local palace-management commands when available.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
