## Description:

青虎AI 短视频数据引擎 batches Douyin, Xiaohongshu, and Bilibili long-form video URLs, collects play, like, share, favorite, and comment metrics, and exports the results as an Excel spreadsheet for owned and competitor video monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Social media operators, ecommerce teams, and agents acting for them use this skill to collect short-video engagement metrics in bulk and export a spreadsheet for daily tracking, competitor monitoring, and downstream performance analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends provided video URLs to Qinghu and may involve user account credentials.

Mitigation: Use only authorized video links, provide a Qinghu API key through qhkit configuration or QHKIT_TOKEN, and avoid sharing unrelated sensitive data in workflow fields.

Risk: Submitting a generate action can spend Qinghu credits.

Mitigation: Run estimate first, present the quoted credit cost and key parameters to the user, and submit only after explicit confirmation.

Risk: Installing or upgrading qhkit and Node can modify the local environment.

Mitigation: Review install prompts, prefer the documented package source, and verify downloaded Node archives with SHA256 before unpacking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shortvideo-data-engine)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash and JSON examples; generated workflow output is an XLSX file link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit and a Qinghu API key; paid generate actions require user confirmation after estimate.]

## Skill Version(s):

0.1.4 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
