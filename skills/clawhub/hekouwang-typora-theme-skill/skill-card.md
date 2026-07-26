## Description: <br>
Helps agents maintain and install the Hekouwang Typora theme by generating light and dark CSS from tokens, sampling reference colors, and verifying font and rendering behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huiyonghkw](https://clawhub.ai/user/huiyonghkw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and theme authors use this skill to edit, build, install, and validate Typora theme variants with token-driven CSS, reference color sampling, and font fallback checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation writes theme CSS and font files under the local Typora themes folder. <br>
Mitigation: Review the install command before running it; the installer backs up existing theme CSS into a subdirectory and is designed to be idempotent. <br>
Risk: The --use-local-anthropic option copies proprietary fonts already installed on the user's machine for personal use only. <br>
Mitigation: Leave the option disabled unless the user understands the font licensing limits; do not redistribute copied proprietary fonts and rely on the bundled Inter fallback for normal releases. <br>
Risk: The publishing workflow includes GitHub commands that act under the user's account. <br>
Mitigation: Review any GitHub publishing commands before execution and confirm repository, branch, and pull request targets. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/huiyonghkw/hekouwang-typora-theme-skill) <br>
- [Token customization guide](references/tokens.md) <br>
- [Typora theme specification notes](references/typora-spec.md) <br>
- [Font strategy and licensing notes](references/fonts.md) <br>
- [Theme workflow guide](references/workflow.md) <br>
- [Typora custom theme documentation](https://theme.typora.io/doc/Write-Custom-Theme/) <br>
- [Hekouwang Typora theme repository](https://github.com/huiyonghkw/hekouwang-typora-theme) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON token edits, and generated CSS files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write Typora theme CSS and font assets to the local Typora themes folder when installation commands are executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter, changelog, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
