## Description: <br>
Edit a Google Slides deck in place from the command line: pull it to editable local SML, change it with semantic selectors, roles, components, images, and layout, preview an exact diff, and push batchUpdates back to the same native, editable deck. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bek91](https://clawhub.ai/user/bek91) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent operators use this skill to create, restyle, QA, and update live Google Slides decks while preserving native editability and Drive version history. It is suited for deck-wide restyles, media and gallery updates, slide creation, cross-deck theme transfer, and batch changes that should be previewed before writing to a deck. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can write changes to live Google Slides decks. <br>
Mitigation: Require explicit confirmation before push, replace-image, reorder, group, or theme-apply operations, and use diff or dry-run first. <br>
Risk: Credential fallback modes may reduce credential-storage protections. <br>
Mitigation: Prefer normal keyring-backed authentication and avoid the insecure credential fallback unless the temporary risk is understood. <br>
Risk: Visual or geometry changes may not match intent after batch updates. <br>
Mitigation: Use diff before push and run check with contact-sheet output to review remote deck renders after changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bek91/skills/slidesmith) <br>
- [slidesmith homepage](https://github.com/unblocklabs-ai/slidesmith) <br>
- [recipes.md](recipes.md) <br>
- [Agent guide](docs/AGENT-GUIDE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, SML snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance commonly includes diff, dry-run, QA, and confirmation steps before commands that write to live Google Slides decks.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
