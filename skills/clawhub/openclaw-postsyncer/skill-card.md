## Description: <br>
Manage your PostSyncer social media workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abakermi](https://clawhub.ai/user/abakermi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to configure PostSyncer access, list workspaces and posts, and create basic text posts for a selected workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a PostSyncer API key that may grant access to social media workflows. <br>
Mitigation: Use a revocable, least-privileged API key when available and avoid exposing it in logs or shared transcripts. <br>
Risk: The skill can create social posts in a selected workspace. <br>
Mitigation: Review workspace IDs and post text before allowing an agent to create or schedule posts. <br>


## Reference(s): <br>
- [PostSyncer Settings](https://app.postsyncer.com/settings) <br>
- [ClawHub skill page](https://clawhub.ai/abakermi/skills/openclaw-postsyncer) <br>
- [Publisher profile](https://clawhub.ai/user/abakermi) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POSTSYNCER_API_KEY; commands can list workspaces and posts and create basic text posts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and target metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
