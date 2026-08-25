## Description:

根据用户提供的电脑/服务器配置清单（图片、截图或文本），在京东平台搜索各配件的价格与商品链接，并生成包含京东链接的 Excel 价格表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuhaorui](https://clawhub.ai/user/wuhaorui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and purchasing or system-building teams use this skill to turn hardware configuration lists from images, screenshots, or text into JD.com price-reference Excel workbooks with product links, subtotals, and notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated spreadsheets may contain fixed or stale prices, links, and item selections that do not match the user's actual hardware list.

Mitigation: Review or modify the helper script and refresh price sources before use; verify JD pages and item details before purchasing.

Risk: The bundled helper script may write output to a developer-specific path instead of the user's workspace.

Mitigation: Set a user-approved workspace output path before running the script.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus Python/openpyxl-generated .xlsx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated pricing should be treated as a reference and verified against current JD pages before purchasing.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
