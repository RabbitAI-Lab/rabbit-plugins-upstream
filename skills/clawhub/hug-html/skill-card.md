## Description: <br>
hug-html helps agents generate and edit self-contained HTML templates from grid layouts, reusable modules, style presets, and optional visual-editor or content-filling workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, designers, and content operators can use this skill to create promotional cards, information panels, interactive calendar dashboards, and reusable grid-based HTML templates. It is intended for generating local HTML artifacts that a user can review, edit, and publish through their own workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: QR-code components may send QR payloads to a third-party QR generation service, which can expose secrets, internal URLs, or sensitive campaign links. <br>
Mitigation: Avoid secrets and internal URLs in QR payloads, and replace remote QR generation with local QR generation before using the output in sensitive environments. <br>
Risk: Generated templates can include raw JavaScript, so opening generated HTML from untrusted template specs can run active web content in the browser. <br>
Mitigation: Review template specs and generated HTML before opening or sharing them, and remove or sandbox custom scripts when the source is not trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/hug-html) <br>
- [User guide](references/guide.md) <br>
- [Module library](references/module-library.md) <br>
- [Architecture](references/architecture.md) <br>
- [Permissions](references/permissions.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and generated self-contained HTML, CSS, and JavaScript files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated HTML may include editable UI behavior, grid specifications, style presets, QR-code components, and user-saved template definitions.] <br>

## Skill Version(s): <br>
3.3.1 (source: frontmatter, _meta.json, release evidence, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
