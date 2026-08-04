## Description: <br>
从微信公众号抓取文章并保存为本地 Markdown 文件，包含图片下载和保存路径汇总。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiongweixp](https://clawhub.ai/user/xiongweixp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch WeChat public-account articles for a named account and date range, then save the converted Markdown and downloaded images locally for later reading, summarization, or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends service AppID/SecureKey values and WeChat lookup details to an external fetch service. <br>
Mitigation: Use environment variables instead of command-line secrets, provide credentials only for this service, and install only when sharing these lookup details is acceptable. <br>
Risk: Article URLs are sent to an external Markdown conversion service. <br>
Mitigation: Avoid private, token-bearing, or confidential URLs unless the external conversion behavior is acceptable for the use case. <br>
Risk: Converted content can trigger automatic image downloads from referenced image URLs. <br>
Mitigation: Run the skill with a narrow output directory and review downloaded files before reusing or sharing the generated Markdown bundle. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiongweixp/skills/wxpublic-fetch) <br>
- [WeChat public account fetch service](https://wxpub.aibana.art/) <br>
- [Markdown conversion service](https://anything-md.doocs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown files with local image references, plus terminal status text listing saved and failed article paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a selected output directory and shared images subdirectory; reports SAVED and FAILED records for downstream agent use.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
