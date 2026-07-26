## Description: <br>
Ai好记 helps agents search, read, export, manage, move, and auto-classify Ai好记 notes and notebooks through the Ai好记 Agent Open Platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aihaoji-agent](https://clawhub.ai/user/aihaoji-agent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Ai好记 users and agents use this skill to search, read, export, organize, move, and auto-classify notes and notebooks in an Ai好记 account. It is suited for workflows that need live account data and explicit confirmation before changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access private Ai好记 notes when configured with an API key. <br>
Mitigation: Install only when account access is intended, use a scoped and revocable API key, and avoid pasting secrets into chat. <br>
Risk: Write operations can export, move, create, rename, or delete notes and notebooks. <br>
Mitigation: Review the proposed change plan and confirmations before allowing exports, moves, notebook creation, renames, or deletes. <br>
Risk: Using guessed or stale IDs could affect the wrong note or notebook. <br>
Mitigation: Use IDs returned by live Ai好记 API queries and re-query the target note or notebook list after changes. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/aihaoji-agent/skills/aihaoji) <br>
- [Server-resolved GitHub source](https://github.com/AiHaoJi-Agent/aihaoji-skills) <br>
- [Ai好记 homepage](https://www.aihaoji.com) <br>
- [Ai好记 Open Platform](https://openapi.aihaoji.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request details, JSON snippets, and confirmation plans.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read or write local API credential configuration and may call Ai好记 Open Platform endpoints when the agent executes the skill.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
