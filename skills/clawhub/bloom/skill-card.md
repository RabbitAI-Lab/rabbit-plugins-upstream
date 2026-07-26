## Description: <br>
Discover your supporter personality and find AI tools you'll love. Get personalized recommendations, connect with your first 100 supporters, and search for skills that match how you work. For indie devs, vibe coders, and AI builders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bloomprotocol](https://clawhub.ai/user/bloomprotocol) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, indie developers, vibe coders, and AI builders use this skill to analyze recent conversation context, generate a supporter identity profile, receive tool recommendations, and create a shareable Bloom identity card. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run downloaded code and npm dependencies at execution time. <br>
Mitigation: Review the source and dependency chain before installation, and pin or audit dependencies before use in managed environments. <br>
Risk: The skill reads conversation sessions and stores derived identity-card data with external Bloom services. <br>
Mitigation: Avoid using the skill on sensitive conversations, and review the generated card before sharing its dashboard link. <br>
Risk: The skill creates persistent configuration and includes wallet/network behavior with limited runtime control. <br>
Mitigation: Replace the default JWT secret before dashboard use, review custody and cleanup behavior, and do not deposit funds into generated wallets until withdrawal behavior is clear. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bloomprotocol/skills/bloom) <br>
- [Bloom Protocol](https://bloomprotocol.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Formatted text or Markdown containing a supporter identity card, profile dimensions, recommendations, dashboard URL, and wallet status notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and npx; may create persistent local configuration and use external network services.] <br>

## Skill Version(s): <br>
2.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
