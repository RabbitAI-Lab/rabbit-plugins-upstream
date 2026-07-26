## Description: <br>
Automate Twitter/X with posting, engagement, and user management via inference.sh CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and social media teams use this skill to generate CLI commands for posting, deleting, liking, retweeting, sending direct messages, following users, and reading Twitter/X account or post details through inference.sh apps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can trigger public or private actions on a live Twitter/X account, including posts, deletes, direct messages, follows, likes, and retweets. <br>
Mitigation: Require explicit human review and approval before each account-changing command is run. <br>
Risk: The quick-start path uses a curl-to-shell installer for the inference.sh CLI. <br>
Mitigation: Prefer manual installation and checksum verification before using the CLI. <br>
Risk: Broad automation triggers could be used for unintended social posting or engagement workflows. <br>
Mitigation: Install only for trusted users and accounts where Twitter/X automation is intentional and governed by local policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/twitter-automation) <br>
- [X.com Integration](https://inference.sh/docs/integrations/x) <br>
- [X.com Integration Example](https://inference.sh/docs/examples/x-integration) <br>
- [Apps Overview](https://inference.sh/docs/apps/overview) <br>
- [CLI checksum verification](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may operate a connected Twitter/X account through inference.sh apps.] <br>

## Skill Version(s): <br>
0.1.5 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
