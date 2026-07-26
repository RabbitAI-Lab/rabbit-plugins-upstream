## Description: <br>
Provides a setup guide for temporary media hosting with seven-day retention, MIME validation, nginx configuration, upload handling, remote fetch helpers, logging, and cleanup scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byron-mckeeby](https://clawhub.ai/user/byron-mckeeby) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to draft or adapt a temporary media-hosting deployment for chat-shared images and videos. It helps configure short retention, MIME checks, public serving, upload handling, remote fetching, statistics, and cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A public media host can expose uploaded files and related access logs beyond the operator's intended audience. <br>
Mitigation: Deploy only on a server intended for public media hosting, document source-IP and source-URL logging, and align retention and privacy expectations before launch. <br>
Risk: Over-broad filesystem permissions can let the web server or upload handler modify more media-hosting state than necessary. <br>
Mitigation: Adjust ownership and directory permissions for least privilege before using the provided setup commands in production. <br>
Risk: Remote fetch helpers can be abused for SSRF, unwanted downloads, or bandwidth consumption if exposed directly. <br>
Mitigation: Do not expose the remote fetch helper publicly unless URL allowlisting, network egress controls, request limits, content checks, and abuse monitoring are in place. <br>
Risk: Cleanup and retention behavior may fail or conflict with operational, legal, or user expectations. <br>
Mitigation: Review the cron cleanup schedule, retention period, log rotation, and failure reporting against the deployment's requirements. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash, nginx, PHP, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup guidance and example snippets; operators must adapt domains, retention, permissions, logging, and abuse controls before deployment.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
