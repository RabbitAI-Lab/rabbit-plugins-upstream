## Description: <br>
Schedule and manage social media posts via the Postiz API for self-hosted or cloud Postiz instances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolmanns](https://clawhub.ai/user/coolmanns) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and content teams use this skill to prepare, schedule, publish, query, update, and delete Postiz-managed social posts across channels such as X/Twitter, LinkedIn, and Bluesky. It is useful for multi-platform posting workflows that need platform-specific content limits, media upload, scheduling, and duplicate checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish or delete posts through a user's Postiz account and connected social channels. <br>
Mitigation: Prefer draft or scheduled posts for first runs, and manually confirm the platform, content, timing, and post IDs before immediate publishing or deletion. <br>
Risk: The helper scripts store a reusable Postiz login cookie at /tmp/postiz-cookies.txt. <br>
Mitigation: Remove or protect the cookie file after use, especially on shared machines. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline bash, JSON, and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Postiz instance, Postiz login credentials, and relevant platform integration IDs.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
