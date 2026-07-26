## Description: <br>
Manage Ghost CMS blog posts through the Ghost Admin API, including creating, updating, deleting, listing, image uploads, and feature images using credentials from a JSON configuration file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to manage posts, tags, images, and feature images on Ghost CMS sites via the Admin API. It supports both command-line and Python workflows when the user supplies a site-specific JSON credential configuration file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish, update, delete, and upload content on a live Ghost site. <br>
Mitigation: Confirm post IDs, titles, status, and intended action before mutating content; prefer draft status unless publication is explicitly requested. <br>
Risk: The skill requires a JSON configuration file containing a Ghost Admin API key. <br>
Mitigation: Keep the configuration file private and rotate the Admin API key if the file or key is exposed. <br>
Risk: Feature-image workflows can download remote URLs before uploading images to Ghost. <br>
Mitigation: Avoid untrusted, private, or internal URLs as feature-image inputs. <br>


## Reference(s): <br>
- [Ghost Admin API Reference](references/api.md) <br>
- [Ghost Official Admin API Documentation](https://ghost.org/docs/admin-api/) <br>
- [ClawHub Skill Page](https://clawhub.ai/manifoldor/skills/ghost) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in Ghost Admin API calls that create, publish, update, delete, list, or upload content when credentials are supplied.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
